import unittest
from app.api.services import create_new_user

class TestIntegration(unittest.TestCase):
    def test_create_user(self):
        user_data = {"username": "testuser"}
        response = create_new_user(user_data)
        self.assertEqual(response["status"], "User added")
