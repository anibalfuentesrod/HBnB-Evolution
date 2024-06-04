from models.base import BaseModel
from models.country import Country

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country