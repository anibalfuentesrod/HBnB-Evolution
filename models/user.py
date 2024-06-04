from models.base import BaseModel

class User(BaseModel):
    email_registry = set()

    def __init__(self, email, password, first_name='', last_name=''):
        if email in User.email_registry:
            raise ValueError("Email already exists")
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.hosted_places = []
        self.reviews = []
        User.email_registry.add(email)
    
    def add_place(self, place):
        if place.host is not None:
            raise ValueError("This place already has a host")
        self.hosted_places.append(place)
        place.host = self