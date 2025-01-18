from concurrent import futures
import grpc
from app.grpc.central_sync_pb2_grpc import add_CentralSyncServicer_to_server, CentralSyncServicer
from app.grpc.central_sync_pb2 import SyncResponse

class CentralSync(CentralSyncServicer):
    def SyncData(self, request, context):
        print(f"Received data: {request.data}")
        return SyncResponse(status="Success")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CentralSyncServicer_to_server(CentralSync(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at localhost:50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
