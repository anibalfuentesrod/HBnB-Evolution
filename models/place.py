from models.base import BaseModel
from models.user import User

class Place(BaseModel):
    def __init__(self, name, descrition, address, city, host, latitude,
                 longitude, number_of_rooms, number_of_bathrooms, price_per_night,
                 max_guests, amenities=[]):
        super().__init__()
        self.name = name
        self.description = descrition
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)