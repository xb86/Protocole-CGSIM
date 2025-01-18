import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestRestApi(unittest.TestCase):
    client = TestClient(app)

    def test_get_user(self):
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("user_id", response.json())
