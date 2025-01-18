from datetime import datetime
from db.models import Client, Transaction
from db.database import db_session
import central_sync_pb2, central_sync_pb2_grpc

class CentralSyncServicer(central_sync_pb2_grpc.CentralSyncServicer):
    
    def CheckCredit(self, request, context):
        client = db_session.query(Client).filter(Client.id == request.client_id).first()
        if client and client.credit > 0:
            return central_sync_pb2.CheckCreditResponse(
                credit_status="valid", credit_amount=client.credit)
        else:
            return central_sync_pb2.CheckCreditResponse(
                credit_status="invalid", credit_amount=0)

    def UseCredit(self, request, context):
        client = db_session.query(Client).filter(Client.id == request.client_id).first()
        if client and client.credit >= request.amount:
            client.credit -= request.amount
            # Enregistrer la transaction avec l'utilisation du crédit
            new_transaction = Transaction(client_id=request.client_id, amount=-request.amount, date=str(datetime.now()))
            db_session.add(new_transaction)
            db_session.commit()
            return central_sync_pb2.UseCreditResponse(status="success", message="Credit used successfully")
        else:
            return central_sync_pb2.UseCreditResponse(status="failed", message="Insufficient credit")

    def AdjustCredit(self, request, context):
        client = db_session.query(Client).filter(Client.id == request.client_id).first()
        if client:
            if client.credit < 0:
                # Vérifier si la date limite est dépassée
                if datetime.now() > client.credit_due_date:
                    client.credit_status = "overdue"
                    db_session.commit()
                    return central_sync_pb2.AdjustCreditResponse(status="Credit overdue")
            return central_sync_pb2.AdjustCreditResponse(status="Credit valid")
        return central_sync_pb2.AdjustCreditResponse(status="Client not found")