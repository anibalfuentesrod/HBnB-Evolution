# HBnB API

This repository contains a RESTful API for managing various entities like users, countries, cities, amenities, and places. The API is built using Flask and stores data in JSON files for persistence.

## Features

- Manage users with the ability to create, retrieve, update, and delete user data.
- Handle country data, including retrieval of all countries and specific country details.
- Manage cities, linking them to countries and supporting CRUD operations.
- Handle amenities, including creating, retrieving, updating, and deleting amenities.
- Manage places, including linking them to cities, hosts, and amenities with full CRUD operations.

## Getting Started

### Setting Up Locally

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

### Setting Up with Docker

To containerize and run the HBnB API using Docker, follow these steps:

1. Ensure Docker is installed on your machine. If not, download and install Docker from [here](https://docs.docker.com/get-docker/).

2. Build the Docker image:

    ```bash
    docker build -t my-flask-app .
    ```

3. Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 -v $(pwd)/data:/app/data my-flask-app
    ```

4. Verify the container is running:

    ```bash
    docker ps
    ```

5. Access the API at [http://localhost:5000](http://localhost:5000).

## Usage

### Users

- **Create a User**

    ```bash
    curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }' | jq
    ```

- **Retrieve All Users**

    ```bash
    curl -X GET http://127.0.0.1:5000/users | jq
    ```

- **Retrieve a Specific User**

    ```bash
    curl -X GET http://127.0.0.1:5000/users/{user_id} | jq
    ```

- **Update a User**

    ```bash
    curl -X PUT http://127.0.0.1:5000/users/{user_id} -H "Content-Type: application/json" -d '{
        "email": "new-email@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }' | jq
    ```

- **Delete a User**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/users/{user_id} | jq
    ```

### Countries

- **Create a Country**

    ```bash
    curl -X POST http://127.0.0.1:5000/countries -H "Content-Type: application/json" -d '{
        "name": "United States",
        "code": "US"
    }' | jq
    ```

- **Retrieve All Countries**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries | jq
    ```

- **Retrieve a Specific Country**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries/{country_code} | jq
    ```

### Cities

- **Create a City**

    ```bash
    curl -X POST http://127.0.0.1:5000/cities -H "Content-Type: application/json" -d '{
        "name": "New York",
        "country_code": "US"
    }' | jq
    ```

- **Retrieve All Cities**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities | jq
    ```

- **Retrieve a Specific City**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities/{city_id} | jq
    ```

- **Update a City**

    ```bash
    curl -X PUT http://127.0.0.1:5000/cities/{city_id} -H "Content-Type: application/json" -d '{
        "name": "New York",
        "country_code": "US"
    }' | jq
    ```

- **Delete a City**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/cities/{city_id} | jq
    ```

### Amenities

- **Create an Amenity**

    ```bash
    curl -X POST http://127.0.0.1:5000/amenities -H "Content-Type: application/json" -d '{
        "name": "Wi-Fi"
    }' | jq
    ```

- **Retrieve All Amenities**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities | jq
    ```

- **Retrieve a Specific Amenity**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities/{amenity_id} | jq
    ```

- **Update an Amenity**

    ```bash
    curl -X PUT http://127.0.0.1:5000/amenities/{amenity_id} -H "Content-Type: application/json" -d '{
        "name": "High-Speed Wi-Fi"
    }' | jq
    ```

- **Delete an Amenity**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/amenities/{amenity_id} | jq
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
    }' | jq
    ```

- **Retrieve All Places**

    ```bash
    curl -X GET http://127.0.0.1:5000/places | jq
    ```

- **Retrieve a Specific Place**

    ```bash
    curl -X GET http://127.0.0.1:5000/places/{place_id} | jq
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
    }' | jq
    ```

- **Delete a Place**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/places/{place_id} | jq
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
