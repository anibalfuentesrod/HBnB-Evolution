from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid
import json
import os

app = Flask(__name__)

data_dir = 'data'

def load_json(file_name):
    with open(os.path.join(data_dir, file_name), 'r') as f:
        return json.load(f)

def save_json(file_name, data):
    with open(os.path.join(data_dir, file_name), 'w') as f:
        json.dump(data, f, indent=4)

# Load databases
users_db = load_json('users.json')
countries_db = load_json('countries.json')
cities_db = load_json('cities.json')
amenities_db = load_json('amenities.json')
places_db = load_json('places.json')

# Validate email format
def is_email_valid(email):
    import re
    email_regex = r'[^@]+@[^@]+\.[^@]+'
    return re.match(email_regex, email) is not None

# Validate country code
def is_valid_country_code(country_code):
    return any(country['code'] == country_code for country in countries_db)

# POST /users: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if not is_email_valid(data['email']):
        return make_response(jsonify({'error': 'Invalid email format'}), 400)
    if any(user['email'] == data['email'] for user in users_db):
        return make_response(jsonify({'error': 'Email already exists'}), 409)
    user_id = str(uuid.uuid4())
    data['id'] = user_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    users_db.append(data)
    save_json('users.json', users_db)
    return make_response(jsonify(data), 201)

# GET /users: Retrieve a list of all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db)

# GET /users/<user_id>: Retrieve details of a specific user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return make_response(jsonify({'error': 'User not found'}), 404)
    return jsonify(user)

# PUT /users/<user_id>: Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return make_response(jsonify({'error': 'User not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    user.update(data)
    user['updated_at'] = datetime.now().isoformat()
    save_json('users.json', users_db)
    return jsonify(user)

# DELETE /users/<user_id>: Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users_db
    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return make_response(jsonify({'error': 'User not found'}), 404)
    users_db = [user for user in users_db if user['id'] != user_id]
    save_json('users.json', users_db)
    return make_response('', 204)

# POST /countries: Create a new country
@app.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    if not data or 'name' not in data or 'code' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if any(country['code'] == data['code'] for country in countries_db):
        return make_response(jsonify({'error': 'Country code already exists'}), 409)
    countries_db.append(data)
    save_json('countries.json', countries_db)
    return make_response(jsonify(data), 201)

# GET /countries: Retrieve all countries
@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(countries_db)

# GET /countries/<country_code>: Retrieve details of a specific country
@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = next((country for country in countries_db if country['code'] == country_code), None)
    if country is None:
        return make_response(jsonify({'error': 'Country not found'}), 404)
    return jsonify(country)

# POST /cities: Create a new city
@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    if not data or 'name' not in data or 'country_code' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if not is_valid_country_code(data['country_code']):
        return make_response(jsonify({'error': 'Invalid country code'}), 400)
    city_id = str(uuid.uuid4())
    data['id'] = city_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    cities_db.append(data)
    save_json('cities.json', cities_db)
    return make_response(jsonify(data), 201)

# GET /cities: Retrieve all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(cities_db)

# GET /cities/<city_id>: Retrieve details of a specific city
@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = next((city for city in cities_db if city['id'] == city_id), None)
    if city is None:
        return make_response(jsonify({'error': 'City not found'}), 404)
    return jsonify(city)

# PUT /cities/<city_id>: Update an existing city
@app.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = next((city for city in cities_db if city['id'] == city_id), None)
    if city is None:
        return make_response(jsonify({'error': 'City not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    city.update(data)
    city['updated_at'] = datetime.now().isoformat()
    save_json('cities.json', cities_db)
    return jsonify(city)

# DELETE /cities/<city_id>: Delete a city
@app.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    global cities_db
    city = next((city for city in cities_db if city['id'] == city_id), None)
    if city is None:
        return make_response(jsonify({'error': 'City not found'}), 404)
    cities_db = [city for city in cities_db if city['id'] != city_id]
    save_json('cities.json', cities_db)
    return make_response('', 204)

# POST /amenities: Creates a new amenity
@app.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data or 'name' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if any(amenity['name'] == data['name'] for amenity in amenities_db):
        return make_response(jsonify({'error': 'Name of amenity already exists'}), 409)
    amenity_id = str(uuid.uuid4())
    data['id'] = amenity_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    amenities_db.append(data)
    save_json('amenities.json', amenities_db)
    return make_response(jsonify(data), 201)

# GET /amenities: Retrieves a list of all amenities
@app.route('/amenities', methods=['GET'])
def get_amenities():
    return jsonify(amenities_db)

# GET /amenities/<amenity_id>: Retrives details of any specific amenity
@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = next((amenity for amenity in amenities_db if amenity['id'] == amenity_id), None)
    if amenity is None:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    return jsonify(amenity)

# PUT /amenities/<amenity_id>: Updates an existing amenity
@app.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = next((amenity for amenity in amenities_db if amenity['id'] == amenity_id), None)
    if amenity is None:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    amenity.update(data)
    amenity['updated_at'] = datetime.now().isoformat()
    save_json('amenities.json', amenities_db)
    return jsonify(amenity)

# DELETE /amenities/<amenity_id>: Deletes a specific amenity
@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    global amenities_db
    amenity = next((amenity for amenity in amenities_db if amenity['id'] == amenity_id), None)
    if amenity is None:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    amenities_db = [amenity for amenity in amenities_db if amenity['id'] != amenity_id]
    save_json('amenities.json', amenities_db)
    return make_response('', 204)

# validate geographical coords
def is_valid_coordinates(lat, lon):
    return -90 <= lat <= 90 and -180 <= lon <= 180

# validate places
def validate_place_data(data):
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
    
    # Check for missing required fields only if it's a creation request
    if 'id' not in data:  # Assuming 'id' is added only during creation
        for field in required_fields:
            if field not in data:
                return False, f'Missing required field: {field}'
    
    # Validate specific fields if they exist in the data
    if 'number_of_rooms' in data and (not isinstance(data['number_of_rooms'], int) or data['number_of_rooms'] < 0):
        return False, 'Invalid number of rooms'
    if 'number_of_bathrooms' in data and (not isinstance(data['number_of_bathrooms'], int) or data['number_of_bathrooms'] < 0):
        return False, 'Invalid number of bathrooms'
    if 'max_guests' in data and (not isinstance(data['max_guests'], int) or data['max_guests'] < 0):
        return False, 'Invalid guest capacity'
    if 'price_per_night' in data and (not isinstance(data['price_per_night'], (int, float)) or data['price_per_night'] < 0):
        return False, 'Invalid price per night'
    if 'latitude' in data and 'longitude' in data and not is_valid_coordinates(data['latitude'], data['longitude']):
        return False, 'Invalid geographical coordinates'
    if 'city_id' in data and data['city_id'] not in [city['id'] for city in cities_db]:
        return False, 'Invalid city_id'
    if 'amenity_ids' in data:
        for amenity_id in data['amenity_ids']:
            if amenity_id not in [amenity['id'] for amenity in amenities_db]:
                return False, f'Invalid amenity_id: {amenity_id}'
    
    return True, None

# POST /places: Creates a new place
@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    is_valid, error = validate_place_data(data)
    if not is_valid:
        return make_response(jsonify({'error': error}), 400)
    place_id = str(uuid.uuid4())
    data['id'] = place_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    places_db.append(data)
    save_json('places.json', places_db)
    return make_response(jsonify(data), 201)

# GET /places: retrieves a list of all places
@app.route('/places', methods=['GET'])
def get_places():
    return jsonify(places_db)

# GET /places/<place_id>: retrives information of a specific place
@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = next((place for place in places_db if place['id'] == place_id), None)
    if place is None:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    return jsonify(place)

# PUT /places/<place_id>: Updates an existing place's information
@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = next((place for place in places_db if place['id'] == place_id), None)
    if place is None:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    place.update(data)
    place['updated_at'] = datetime.now().isoformat()
    is_valid, error = validate_place_data(place)
    if not is_valid:
        return make_response(jsonify({'error': error}), 400)
    save_json('places.json', places_db)
    return jsonify(place)

# DELETE /places/<place_id>: Deletes a specific place
@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    global places_db
    place = next((place for place in places_db if place['id'] == place_id), None)
    if place is None:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    places_db = [place for place in places_db if place['id'] != place_id]
    save_json('places.json', places_db)
    return make_response('', 204)

if __name__ == '__main__':
    app.run(debug=True)
