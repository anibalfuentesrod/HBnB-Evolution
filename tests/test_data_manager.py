import unittest
import json
import uuid
from data_manager import DataManager

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager('data/storage.json')

    def test_save_and_get_user(self):
        user_id = str(uuid.uuid4())
        user_data = {
            "id": user_id,
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "created_at": "2024-06-14T00:00:00",
            "updated_at": "2024-06-14T00:00:00"
        }
        self.data_manager.save('users', user_id, user_data)
        user = self.data_manager.get('users', user_id)
        self.assertEqual(user['email'], "testuser@example.com")

    def test_update_user(self):
        user_id = str(uuid.uuid4())
        user_data = {
            "id": user_id,
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "created_at": "2024-06-14T00:00:00",
            "updated_at": "2024-06-14T00:00:00"
        }
        self.data_manager.save('users', user_id, user_data)
        updated_user_data = user_data.copy()
        updated_user_data['email'] = "newemail@example.com"
        self.data_manager.update('users', user_id, updated_user_data)
        user = self.data_manager.get('users', user_id)
        self.assertEqual(user['email'], "newemail@example.com")

    def test_delete_user(self):
        user_id = str(uuid.uuid4())
        user_data = {
            "id": user_id,
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "created_at": "2024-06-14T00:00:00",
            "updated_at": "2024-06-14T00:00:00"
        }
        self.data_manager.save('users', user_id, user_data)
        self.data_manager.delete('users', user_id)
        user = self.data_manager.get('users', user_id)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
