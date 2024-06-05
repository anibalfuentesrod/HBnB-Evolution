from persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_id not in self.storage:
            self.storage[entity_id] = {}
        self.storage[entity_id][entity_type] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_id, {}).get(entity_type, None)

    def update(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_id in self.storage and entity_type in self.storage[entity_id]:
            self.storage[entity_id][entity_type] = entity

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage and entity_type in self.storage[entity_id]:
            del self.storage[entity_id][entity_type]
            if not self.storage[entity_id]:
                del self.storage[entity_id]
