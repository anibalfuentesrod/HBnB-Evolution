import json
import os
from persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.storage = self.load_storage()

    def save(self, entity_type, entity_id, entity_data):
        """Save an entity to the storage."""
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity_data
        self.save_storage()

    def get(self, entity_type, entity_id):
        """Retrieve an entity by ID from the storage."""
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity_type, entity_id, entity_data):
        """Update an entity in the storage."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity_data
            self.save_storage()
            return True
        return False

    def delete(self, entity_type, entity_id):
        """Delete an entity from the storage."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_storage()
            return True
        return False

    def get_all(self, entity_type):
        """Retrieve all entities of a specific type from the storage."""
        return list(self.storage.get(entity_type, {}).values())

    def save_storage(self):
        """Save the storage to the file."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.storage, f, indent=4)

    def load_storage(self):
        """Load the storage from the file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return {}

# Initialize DataManager instance
data_manager = DataManager('data/storage.json')