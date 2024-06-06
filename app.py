from flask import Flask, request, jsonify, make_response
import uuid
from datetime import datetime

app = Flask(__name__)

# Pre-loaded country data based on ISO 3166-1 standard with alpha-2 codification
countries_db = {
    'US': {'name': 'United States', 'code': 'US'},
    'CA': {'name': 'Canada', 'code': 'CA'},
    'MX': {'name': 'Mexico', 'code': 'MX'}
}

# Placeholder for city data
cities_db = {}

# Helper function to validate country code
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
