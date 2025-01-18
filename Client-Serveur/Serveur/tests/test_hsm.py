import unittest
from app.hsm.hsm_manager import generate_key

class TestHsm(unittest.TestCase):
    def test_generate_key(self):
        key = generate_key()
        self.assertIsNotNone(key)
