# gRPC Specification

Le protocole gRPC est utilisé pour la communication entre les magasins et le serveur central pour la synchronisation des informations de crédit. Le service principal est défini dans le fichier `central_sync.proto`.

## Services
- **CentralSync** : Service permettant la synchronisation des informations de crédit.

### Méthodes
- **SyncCreditInfo** :
  - **Requête** : 
    ```protobuf
    message SyncCreditRequest {
      string user_id = 1;
      float amount = 2;
      string store_id = 3;
      string transaction_id = 4;
    }
    ```
  - **Réponse** : 
    ```protobuf
    message SyncCreditResponse {
      bool success = 1;
      string message = 2;
    }
    ```

## Utilisation
Utilisation du client gRPC dans le code Python :
```python
import grpc
from .generated import central_sync_pb2, central_sync_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = central_sync_pb2_grpc.CentralSyncStub(channel)

request = central_sync_pb2.SyncCreditRequest(
    user_id='12345', amount=50.0, store_id='A32', transaction_id='T123'
)
response = stub.SyncCreditInfo(request)
print(response.success, response.message)
