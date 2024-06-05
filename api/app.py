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

if __name__ == '__main__':
    app.run(debug=True)

# Write the Flask app code to a new file
with open(flask_app_path, 'w') as file:
    file.write(flask_app_code)

flask_app_path
