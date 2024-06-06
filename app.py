from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock databases for demonstration
users_db = {}
countries_db = {}
cities_db = {}

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

if __name__ == '__main__':
    app.run(debug=True)
