from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock databases for demonstration
users_db = {}
countries_db = {}
cities_db = {}
amenities_db = {}
places_db = {}

# Validate email format
def is_email_valid(email):
    import re
    email_regex = r'[^@]+@[^@]+\.[^@]+'
    return re.match(email_regex, email) is not None

# Validate country code
def is_valid_country_code(country_code):
    return country_code in countries_db

# POST /users: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if not is_email_valid(data['email']):
        return make_response(jsonify({'error': 'Invalid email format'}), 400)
    if data['email'] in users_db:
        return make_response(jsonify({'error': 'Email already exists'}), 409)
    user_id = str(uuid.uuid4())
    data['id'] = user_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    users_db[user_id] = data
    return make_response(jsonify(data), 201)

# GET /users: Retrieve a list of all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users_db.values()))

# GET /users/<user_id>: Retrieve details of a specific user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users_db:
        return make_response(jsonify({'error': 'User not found'}), 404)
    return jsonify(users_db[user_id])

# PUT /users/<user_id>: Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users_db:
        return make_response(jsonify({'error': 'User not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    users_db[user_id].update(data)
    users_db[user_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(users_db[user_id])

# DELETE /users/<user_id>: Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users_db:
        return make_response(jsonify({'error': 'User not found'}), 404)
    del users_db[user_id]
    return make_response('', 204)

# POST /countries: Create a new country
@app.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    if not data or 'name' not in data or 'code' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if data['code'] in countries_db:
        return make_response(jsonify({'error': 'Country code already exists'}), 409)
    countries_db[data['code']] = data
    return make_response(jsonify(data), 201)

# GET /countries: Retrieve all countries
@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(list(countries_db.values()))

# GET /countries/<country_code>: Retrieve details of a specific country
@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    if country_code not in countries_db:
        return make_response(jsonify({'error': 'Country not found'}), 404)
    return jsonify(countries_db[country_code])

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
    cities_db[city_id] = data
    return make_response(jsonify(data), 201)

# GET /cities: Retrieve all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(list(cities_db.values()))

# GET /cities/<city_id>: Retrieve details of a specific city
@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    return jsonify(cities_db[city_id])

# PUT /cities/<city_id>: Update an existing city
@app.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    cities_db[city_id].update(data)
    cities_db[city_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(cities_db[city_id])

# DELETE /cities/<city_id>: Delete a city
@app.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    del cities_db[city_id]
    return make_response('', 204)

# POST /amenities: Creates a new amenity
@app.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data or 'name' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if any(amenity['name'] == data['name'] for amenity in amenities_db.values()):
        return make_response(jsonify({'error': 'Name of amenity already exists'}), 409)
    amenity_id = str(uuid.uuid4())
    data['id'] = amenity_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    amenities_db[amenity_id] = data
    return make_response(jsonify(data), 201)

# GET /amenities: Retrieves a list of all amenities
@app.route('/amenities', methods=['GET'])
def get_amenities():
    return jsonify(list(amenities_db.values()))

# GET /amenities/<amenity_id>: Retrives details of any specific amenity
@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    if amenity_id not in amenities_db:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    return jsonify(amenities_db[amenity_id])

# PUT /amenities/<amenity_id>: Updates an existing amenity
@app.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    if amenity_id not in amenities_db:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    amenities_db[amenity_id].update(data)
    amenities_db[amenity_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(amenities_db[amenity_id])

# DELETE /amenities/<amenity_id>: Deletes a specific amenity
@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    if amenity_id not in amenities_db:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)
    del amenities_db[amenity_id]
    return make_response('', 204)

# Validate country code
def is_valid_country_code(country_code):
    return country_code in countries_db

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
    if 'city_id' in data and data['city_id'] not in cities_db:
        return False, 'Invalid city_id'
    if 'amenity_ids' in data:
        for amenity_id in data['amenity_ids']:
            if amenity_id not in amenities_db:
                return False, f'Invalid amenity_id: {amenity_id}'
    
    return True, None

# POST /places: Creates a new place
@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    is_valid, error = validate_place_data(data)
    if not is_valid:
        return make_response(jsonify({'error': 'Invalid input'}), 400)
    place_id = str(uuid.uuid4())
    data['id'] = place_id
    data['created_at'] = data['updated_at'] = datetime.now().isoformat()
    places_db[place_id] = data
    return make_response(jsonify(data), 201)

# GET /places: retrieves a list of all places
@app.route('/places', methods=['GET'])
def get_places():
    return jsonify(list(places_db.values()))

# GET /places/<place_id>: retrives information of a specific place
@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    if place_id not in places_db:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    return jsonify(places_db[place_id])

# PUT /places/<place_id>: Updates an existing place's information
@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    if place_id not in places_db:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    current_data = places_db[place_id].copy()
    for key, value in data.items():
        places_db[place_id][key] = value
    is_valid, error = validate_place_data(places_db[place_id])
    if not is_valid:
        places_db[place_id] = current_data
        return make_response(jsonify({'error' : 'Invalid input'}), 400)

    places_db[place_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(places_db[place_id]), 200

# DELETE /places/<place_id>: Deletes a specific place
@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_id not in places_db:
        return make_response(jsonify({'error': 'Place not found'}), 404)
    del places_db[place_id]
    return make_response('', 204)

if __name__ == '__main__':
    app.run(debug=True)
