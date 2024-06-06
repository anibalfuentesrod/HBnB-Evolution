import json
from persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, storage_file='storage.json'):
        self.storage_file = storage_file
        self.storage = self.load_storage()

    def save(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_id not in self.storage:
            self.storage[entity_id] = {}
        self.storage[entity_id][entity_type] = entity.__dict__
        self.save_storage()

    def get(self, entity_id, entity_type):
        entity_data = self.storage.get(entity_id, {}).get(entity_type, None)
        if entity_data:
            return entity_data
        return None

    def update(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_id in self.storage and entity_type in self.storage[entity_id]:
            self.storage[entity_id][entity_type] = entity.__dict__
            self.save_storage()

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage and entity_type in self.storage[entity_id]:
            del self.storage[entity_id][entity_type]
            if not self.storage[entity_id]:
                del self.storage[entity_id]
            self.save_storage()

    def save_storage(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.storage, f)

    def load_storage(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

