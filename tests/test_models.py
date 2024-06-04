import unittest
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country

class TestModels(unittest.TestCase):

    def test_user_creation(self):
        user = User(email="test@example.com", password="password")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")

    def test_place_creation(self):
        user = User(email="host@example.com", password="password")
        place = Place(name="Test Place", host=user, description="A place to stay")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "A place to stay")
        self.assertEqual(place.host, user)

    def test_add_review(self):
        user = User(email="reviewer@example.com", password="password")
        place = Place(name="Test Place", host=user, description="A place to stay")
        review = Review(user=user, place=place, rating=5, comment="Great place!")
        place.reviews.append(review)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], review)

    def test_city_country(self):
        country = Country(name="Test Country")
        city = City(name="Test city", country=country)
        self.assertEqual(city.name, "Test city")
        self.assertEqual(city.country, country)

if __name__ == '__main__':
    unittest.main()
