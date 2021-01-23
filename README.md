# Casting Agency Capstone Project

The project is a webpage for Casting Agency Company that is responsible for creating movies and managing and assigning actors to those movies. 
This project will provide these functionality below:

1) Display movies and actors.
2) Delete movies and actors.
3) Add movie and actor.
4) Modify movie and actor.

# Casting Agency API Backend

The `./backend` directory contains Flask and SQLAlchemy server in app.py we define the endpoints and reference models.py for DB and SQLAlchemy setup. 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 405: method not allowed

## Models

- Movies with attributes title and release date
- Actors with attributes name, age and gender
- movie_actor is an association table to join the two tables together, storing two foreign keys movie_id and actor_id.

## Roles:

### 1) Casting Assistant
  - Can view actors and movies

### 2) Casting Director
- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
Modify actors or movies

### 3) Executive Producer
- All permissions a Casting Director has and…
- Add or delete a movie from the database


## Endpoints

#### GET /movies
 - General:
    - Returns a list of movie objects, success value.
 - Sample:
    we can use Curl command or using Postman
 ```
  curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:5000/movies

  ```
  ```
{
  "movies": [
    {
      "id": 1, 
      "release_date": "Sun, 11 Oct 2020 00:00:00 GMT", 
      "title": "WooW"
    }, 
    {
      "id": 3, 
      "release_date": "Fri, 27 Oct 2023 00:00:00 GMT", 
      "title": "ggg"
    }
  ], 
  "success": true
}
  ```

#### GET /actors
 - General:
    - Return a list of actors.
 - Sample:
 ```
 curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:5000/actors
  ```
  ```
{
  "actors": [
    {
      "age": 30, 
      "gender": "male", 
      "id": 2, 
      "name": "saad"
    }, 
    {
      "age": 10, 
      "gender": "male", 
      "id": 1, 
      "name": "elyas"
    }
  ], 
  "success": true
}
  ```

#### DELETE /actors/{actor_id}
 - General:
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor, success value.
 - Sample:
 ```
  curl -X DELETE -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:5000/actors/4
  ```
  ```
{
  "deleted_actor_id": 4, 
  "success": true
}
  ```

  #### POST /actors
 - General:
    - Creates a new actor using the submitted name, gender and age. Returns the new actor object, the id of the created actor and success value.
 - Sample:
 ```
  curl -X POST -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors -d '{"name":"Gorge", "gender":"male", "age":30}'
  ```
  ```
{
  "new_actor": {
    "age": 30, 
    "gender": "male", 
    "id": 11, 
    "name": "Gorge"
  }, 
  "new_actor_id": 11, 
  "success": true
}
  ```
 #### PATCH /actors
 - General:
    - Modify the specific actor. Returns the updated actor object, the id of this actor and success value.
 - Sample:
 ```
  curl -X PATCH -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors/11 -d '{"name":"Rayen", "gender":"male", "age":30}'
  ```
  ```
{
  "actor": {
    "age": 30, 
    "gender": "male", 
    "id": 11, 
    "name": "Rayen"
  }, 
  "success": true, 
  "updated_actor_id": 11
}
  ```
the endpoints for movies they are same for actors.

## Testing
To run the tests, run
```
dropdb casting_agency_test
createdb casting_agency_test
python3 test_app.py
```