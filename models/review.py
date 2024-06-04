from models.base import BaseModel


class Reviews(BaseModel):
    def __init__(self, user, place, text, rating):
        super().__init__()
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        