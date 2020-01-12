# CASTING AGENCY

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

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the casting_agency.psql file provided. From the backend folder in terminal run:

```bash
psql casting_agency < casting_agency.psql
```

## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

To run the server for test, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file

```

Endpoints

GET '/actors'
- Fetches a dictionary of actors in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, actors, that contains a object of key:value pairs.
{
  "actors": [
    {
      "age": 23,
      "gender": "male",
      "id": 1,
      "name": "James Blonder"
    },
    {
      "age": 23,
      "gender": "male",
      "id": 2,
      "name": "James Blond"
    },
  ],
  "success": true,
  "total_actors": 2
}
----------------------------------------------------------------------------------------------------
GET '/movies'
- Fetches a list of all movies the database
- Request Arguments: None
- Returns: An object with a keys; categories, movies and total_movies
{
  "movies": [
    {
      "id": 1,
      "release_date": "Sat, 02 Feb 2019 00:00:00 GMT",
      "title": "Witcher"
    },
    {
      "id": 2,
      "release_date": "Mon, 03 Mar 2014 00:00:00 GMT",
      "title": "Merlin"
    }
  ],
  "success": true,
  "total_movies": 2
}
----------------------------------------------------------------------------------------------------
POST '/actors'
- Creates a new actor in the database
- Request Arguments:
        {
            "name": <str>,
            "gender": <str>,
            "age": <int>
        }
- Returns: A dictionary containing a success message if the operation was successful
{
  "created": 1,
  "message": "Actor created",
  "success": true
}
----------------------------------------------------------------------------------------------------
POST '/movies'
- Creates a new movie in the database
- Request Arguments:
        {
            "title": <str>,
            "release_date": <str>,
        }
- Returns: A dictionary containing a success message if the operation was successful
{
  "created": 1,
  "message": "Movie created",
  "success": true
}

-------------------------------------------------------------------------------------------------------
PATCH '/actors/{actor_id}'
- Edits an actor  from the database
- Request Arguments: actor_id
- Returns: A dictionary containing a success message if the operation was successful

{
  "actor": [
    {
      "age": 23,
      "gender": "male",
      "id": 1,
      "name": "James Blonder"
    }
  ],
  "success": true
}
-------------------------------------------------------------------------------------------------------
PATCH '/movies/{movie_id}'
- Edits a movie from the database
- Request Arguments: movie_id
- Returns: A dictionary containing a success message if the operation was successful

{
  "movie": [
    {
      "id": 2,
      "release_date": "Sat, 02 Feb 2019 00:00:00 GMT",
      "title": "Witcher"
    }
  ],
  "success": true
}
-------------------------------------------------------------------------------------------------------
DELETE '/actors/{actor_id}'
- Deletes an actor from the database
- Request Arguments: actor_id
- Returns: A dictionary containing a success message if the operation was successful

{
  "deleted": 2,
  "message": "Actor deleted",
  "success": true
}
-------------------------------------------------------------------------------------------------------
DELETE '/movies/{movie_id}'
- Deletes a movie from the database
- Request Arguments: movie_id
- Returns: A dictionary containing a success message if the operation was successful

{
  "deleted": 2,
  "message": "Movie deleted",
  "success": true
}

## Testing

To run the tests, run

```

dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test < casting_agency_test.psql
python test.py

```

```
