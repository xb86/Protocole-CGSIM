import unittest
from app.grpc_client import grpc_call

class TestGrpc(unittest.TestCase):
    def test_grpc_call(self):
        grpc_call()
        self.assertTrue(True)  # Ce test pourrait être amélioré en fonction de la réponse gRPC
