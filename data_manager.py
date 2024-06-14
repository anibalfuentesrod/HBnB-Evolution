from persistence_manager import IPersistenceManager
import json
import os

class DataManager(IPersistenceManager):
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.storage = self.load_storage()

    def save(self, entity_type, entity):
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity['id']] = entity
        self.save_storage()

    def get(self, entity_type, entity_id):
        return self.storage.get(entity_type, {}).get(entity_id, None)

    def update(self, entity_type, entity_id, entity):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            self.save_storage()
            return True
        return False

    def delete(self, entity_type, entity_id):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_storage()
            return True
        return False

    def get_all(self, entity_type):
        return list(self.storage.get(entity_type, {}).values())

    def save_storage(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.storage, f, indent=4)

    def load_storage(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

data_manager = DataManager('data/storage.json')
