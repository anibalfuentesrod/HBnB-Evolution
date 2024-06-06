# Path to save the new Flask application Python script
flask_app_path = os.path.join(inner_extract_dir, 'api', 'app.py')

# Content of the Flask app
from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database for demonstration
users_db = {}

# Validate email
def is_email_valid(email):
    import re
    email_regex = r'[^@]+@[^@]+\\.[^@]+'
    return re.match(email_regex, email) is not None

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

# Mock database for demonstration (task 4)
users_db = {}
countries_db = {
    'US': {'name': 'United States', 'code': 'US'},
    'CA': {'name': 'Canada', 'code': 'CA'},
    'MX': {'name': 'Mexico', 'code': 'MX'}
}
cities_db = {}

# Helper functions
def validate_country_code(code):
    return code in countries_db

# Country Endpoints
@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(list(countries_db.values()))

@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    if country_code not in countries_db:
        return make_response(jsonify({'error': 'Country not found'}), 404)
    return jsonify(countries_db[country_code])

@app.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    if not validate_country_code(country_code):
        return make_response(jsonify({'error': 'Invalid country code'}), 400)
    filtered_cities = [city for city in cities_db.values() if city['country_code'] == country_code]
    return jsonify(filtered_cities)

# City Endpoints
@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    if not data or 'name' not in data or 'country_code' not in data:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    if not validate_country_code(data['country_code']):
        return make_response(jsonify({'error': 'Invalid country code'}), 400)
    for city in cities_db.values():
        if city['name'] == data['name'] and city['country_code'] == data['country_code']:
            return make_response(jsonify({'error': 'City name must be unique within the same country'}), 409)
    city_id = str(uuid.uuid4())
    data.update({'id': city_id, 'created_at': datetime.now().isoformat(), 'updated_at': datetime.now().isoformat()})
    cities_db[city_id] = data
    return make_response(jsonify(data), 201)

@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(list(cities_db.values()))

@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    return jsonify(cities_db[city_id])

@app.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)
    if 'country_code' in data and not validate_country_code(data['country_code']):
        return make_response(jsonify({'error': 'Invalid country code'}), 400)
    cities_db[city_id].update(data)
    cities_db[city_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(cities_db[city_id])

@app.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    if city_id not in cities_db:
        return make_response(jsonify({'error': 'City not found'}), 404)
    del cities_db[city_id]
    return make_response('', 204)


if __name__ == '__main__':
    app.run(debug=True)

# Write the Flask app code to a new file
with open(flask_app_path, 'w') as file:
    file.write(flask_app_code)

flask_app_path
