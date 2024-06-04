import uuid
from datetime import datetime

class Place:
    def __init__(self, name, host, description="", address="", city=None, latitude=0.0, longitude=0.0, 
                 number_of_rooms=0, bathrooms=0, price_per_night=0.0, max_guests=0, amenities=None, reviews=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities or []
        self.reviews = reviews or []
