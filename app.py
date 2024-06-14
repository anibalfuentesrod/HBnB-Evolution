from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid
from data_manager import data_manager

app = Flask(__name__)

# User endpoints
@app.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def manage_users():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('users'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data['created_at'] = data['updated_at'] = datetime.now().isoformat()
        data_manager.save('users', data)
        return make_response(jsonify(data), 201)

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_user(user_id):
    user = data_manager.get('users', user_id)
    if not user:
        return make_response(jsonify({'error': 'User not found'}), 404)

    if request.method == 'GET':
        return jsonify(user)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = user_id
        data['updated_at'] = datetime.now().isoformat()
        data_manager.update('users', user_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('users', user_id)
        return make_response('', 204)

# Country endpoints
@app.route('/countries', methods=['GET', 'POST'], strict_slashes=False)
def manage_countries():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('countries'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data or 'code' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data_manager.save('countries', data)
        return make_response(jsonify(data), 201)

@app.route('/countries/<country_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_country(country_id):
    country = data_manager.get('countries', country_id)
    if not country:
        return make_response(jsonify({'error': 'Country not found'}), 404)

    if request.method == 'GET':
        return jsonify(country)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = country_id
        data_manager.update('countries', country_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('countries', country_id)
        return make_response('', 204)

# City endpoints
@app.route('/cities', methods=['GET', 'POST'], strict_slashes=False)
def manage_cities():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('cities'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data or 'country_code' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data_manager.save('cities', data)
        return make_response(jsonify(data), 201)

@app.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_city(city_id):
    city = data_manager.get('cities', city_id)
    if not city:
        return make_response(jsonify({'error': 'City not found'}), 404)

    if request.method == 'GET':
        return jsonify(city)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = city_id
        data_manager.update('cities', city_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('cities', city_id)
        return make_response('', 204)

# Amenity endpoints
@app.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def manage_amenities():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('amenities'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data_manager.save('amenities', data)
        return make_response(jsonify(data), 201)

@app.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_amenity(amenity_id):
    amenity = data_manager.get('amenities', amenity_id)
    if not amenity:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)

    if request.method == 'GET':
        return jsonify(amenity)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = amenity_id
        data['updated_at'] = datetime.now().isoformat()
        data_manager.update('amenities', amenity_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('amenities', amenity_id)
        return make_response('', 204)

# Place endpoints
@app.route('/places', methods=['GET', 'POST'], strict_slashes=False)
def manage_places():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('places'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'address' not in data or 'city_id' not in data or 'latitude' not in data or 'longitude' not in data or 'host_id' not in data or 'number_of_rooms' not in data or 'number_of_bathrooms' not in data or 'price_per_night' not in data or 'max_guests' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data['created_at'] = data['updated_at'] = datetime.now().isoformat()
        data_manager.save('places', data)
        return make_response(jsonify(data), 201)

@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_place(place_id):
    place = data_manager.get('places', place_id)
    if not place:
        return make_response(jsonify({'error': 'Place not found'}), 404)

    if request.method == 'GET':
        return jsonify(place)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = place_id
        data['updated_at'] = datetime.now().isoformat()
        data_manager.update('places', place_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('places', place_id)
        return make_response('', 204)

# Review endpoints
@app.route('/reviews', methods=['GET', 'POST'], strict_slashes=False)
def manage_reviews():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('reviews'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'place_id' not in data or 'user_id' not in data or 'rating' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data['created_at'] = data['updated_at'] = datetime.now().isoformat()
        data_manager.save('reviews', data)
        return make_response(jsonify(data), 201)

@app.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_review(review_id):
    review = data_manager.get('reviews', review_id)
    if not review:
        return make_response(jsonify({'error': 'Review not found'}), 404)

    if request.method == 'GET':
        return jsonify(review)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = review_id
        data['updated_at'] = datetime.now().isoformat()
        data_manager.update('reviews', review_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('reviews', review_id)
        return make_response('', 204)

if __name__ == '__main__':
    app.run(debug=True)
