
# HBnB API

This repository contains a RESTful API for managing various entities like users, countries, cities, amenities, and places. The API is built using Flask and stores data in JSON files for persistence.

## Features

- Manage users with the ability to create, retrieve, update, and delete user data.
- Handle country data, including retrieval of all countries and specific country details.
- Manage cities, linking them to countries and supporting CRUD operations.
- Handle amenities, including creating, retrieving, updating, and deleting amenities.
- Manage places, including linking them to cities, hosts, and amenities with full CRUD operations.

## Getting Started

To set up and run the HBnB API on your local machine, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/hbnb-api.git
    ```

2. Navigate to the project directory and set up a virtual environment:

    ```bash
    cd hbnb-api
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    flask run
    ```

## Usage

### Users

- **Create a User**

    ```bash
    curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }'
    ```

- **Retrieve All Users**

    ```bash
    curl -X GET http://127.0.0.1:5000/users
    ```

- **Retrieve a Specific User**

    ```bash
    curl -X GET http://127.0.0.1:5000/users/{user_id}
    ```

- **Update a User**

    ```bash
    curl -X PUT http://127.0.0.1:5000/users/{user_id} -H "Content-Type: application/json" -d '{
        "email": "new-email@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }'
    ```

- **Delete a User**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/users/{user_id}
    ```

### Countries

- **Create a Country**

    ```bash
    curl -X POST http://127.0.0.1:5000/countries -H "Content-Type: application/json" -d '{
        "name": "United States",
        "code": "US"
    }'
    ```

- **Retrieve All Countries**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries
    ```

- **Retrieve a Specific Country**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries/{country_code}
    ```

### Cities

- **Create a City**

    ```bash
    curl -X POST http://127.0.0.1:5000/cities -H "Content-Type: application/json" -d '{
        "name": "New York",
        "country_code": "US"
    }'
    ```

- **Retrieve All Cities**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities
    ```

- **Retrieve a Specific City**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities/{city_id}
    ```

- **Update a City**

    ```bash
    curl -X PUT http://127.0.0.1:5000/cities/{city_id} -H "Content-Type: application/json" -d '{
        "name": "New York",
        "country_code": "US"
    }'
    ```

- **Delete a City**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/cities/{city_id}
    ```

### Amenities

- **Create an Amenity**

    ```bash
    curl -X POST http://127.0.0.1:5000/amenities -H "Content-Type: application/json" -d '{
        "name": "Wi-Fi"
    }'
    ```

- **Retrieve All Amenities**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities
    ```

- **Retrieve a Specific Amenity**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities/{amenity_id}
    ```

- **Update an Amenity**

    ```bash
    curl -X PUT http://127.0.0.1:5000/amenities/{amenity_id} -H "Content-Type: application/json" -d '{
        "name": "High-Speed Wi-Fi"
    }'
    ```

- **Delete an Amenity**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/amenities/{amenity_id}
    ```

### Places

- **Create a Place**

    ```bash
    curl -X POST http://127.0.0.1:5000/places -H "Content-Type: application/json" -d '{
        "name": "Central Park",
        "description": "A large public park in New York City.",
        "address": "New York, NY",
        "city_id": "<city-id>",
        "latitude": 40.785091,
        "longitude": -73.968285,
        "host_id": "<user-id>",
        "number_of_rooms": 0,
        "number_of_bathrooms": 0,
        "price_per_night": 0,
        "max_guests": 100,
        "amenity_ids": ["<amenity-id>"]
    }'
    ```

- **Retrieve All Places**

    ```bash
    curl -X GET http://127.0.0.1:5000/places
    ```

- **Retrieve a Specific Place**

    ```bash
    curl -X GET http://127.0.0.1:5000/places/{place_id}
    ```

- **Update a Place**

    ```bash
    curl -X PUT http://127.0.0.1:5000/places/{place_id} -H "Content-Type: application/json" -d '{
        "name": "Updated Park",
        "description": "An updated description.",
        "address": "Updated Address, NY",
        "city_id": "<city-id>",
        "latitude": 40.785091,
        "longitude": -73.968285,
        "host_id": "<user-id>",
        "number_of_rooms": 0,
        "number_of_bathrooms": 0,
        "price_per_night": 0,
        "max_guests": 100,
        "amenity_ids": ["<amenity-id>"]
    }'
    ```

- **Delete a Place**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/places/{place_id}
    ```

## Running the Server

To run the Flask server, use the following command:
```bash
flask run
```

Ensure you have Flask installed in your virtual environment and that you are in the directory where your `app.py` file is located.

## Data Persistence

The data for users, countries, cities, amenities, and places are persisted in JSON files. These files are updated whenever a create, update, or delete operation is performed on any entity.

## Testing the API

You can use tools like `curl`, Postman, or any other API testing tool to interact with the endpoints and verify their functionality.

## Authors

- Anibal Fuentes
- Luis Soto
- Steven Rosario
