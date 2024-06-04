import uuid
from datetime import datetime

class Review:
    def __init__(self, user, place, rating, comment=""):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment