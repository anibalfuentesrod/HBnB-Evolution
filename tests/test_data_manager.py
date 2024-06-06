import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_manager import DataManager
from models.user import User

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.test_storage_file = 'test_storage.json'
        self.data_manager = DataManager(storage_file=self.test_storage_file)
        User.clear_existing_emails()

    def tearDown(self):
        if os.path.exists(self.test_storage_file):
            os.remove(self.test_storage_file)

    def test_save_and_get_user(self):
        user = User(email="anibal@gmail.com", password="anibal321")
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], "anibal@gmail.com")

    def test_update_user(self):
        user = User(email="anibal@gmail.com", password="anibal321")
        self.data_manager.save(user)
        user.password = "anibalnew"
        self.data_manager.update(user)
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['password'], "anibalnew")

    def test_delete_user(self):
        user = User(email="test@example.com", password="password")
        self.data_manager.save(user)
        self.data_manager.delete(user.id, 'User')
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()
