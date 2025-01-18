import grpc
from app.grpc.central_sync_pb2 import SyncRequest
from app.grpc.central_sync_pb2_grpc import CentralSyncStub
from app.grpc import central_sync_pb2, central_sync_pb2_grpc

def grpc_call():
    channel = grpc.insecure_channel('localhost:50051')
    stub = CentralSyncStub(channel)
    request = SyncRequest(data="test")
    response = stub.SyncData(request)
    print("Response: ", response)

def check_credit(client_id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = central_sync_pb2_grpc.CentralSyncStub(channel)
        request = central_sync_pb2.CheckCreditRequest(client_id=client_id)
        response = stub.CheckCredit(request)
        return response

def process_credit_usage(client_id, amount_to_use):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = central_sync_pb2_grpc.CentralSyncStub(channel)
        request = central_sync_pb2.UseCreditRequest(client_id=client_id, amount=amount_to_use)
        response = stub.UseCredit(request)
        return response