# Capstone-kml

## Description

This project demonstrates what we have learned in the Udacity Full Stack Web Developer nano degree course.  
It enables users to create, view, update and delete actors and movies.  
The backend is designed to work for three types of users: Casting Assistant, Casting Director, and Executive Producers. 

Executive Producers are super users, and can create, view, update and delete actors and movies.  
A Casting Assistant can only view actors and mocies.  Casting Director can create, view, update and delete actors, 
but can only view or update movies. Users must be authorized to be able to perform role-based requests to the backend via API described below. 

Authorization of users is enabled via Auth0 in which two seperate roles (companies and candidates) have been created 
and assigned seperate permissions. 

## Project dependencies

The project depends on the latest version of Python 3.x which we recommend to download 
and install from their official website and use a virtual environment to install all dependencies.

## PIP dependencies

After having successfully installed Python, navigate to the root folder of the project 
(the project must be forked to your local machine) and run the following in a command line:

```
pip3 install -r requirements.txt
```

This will install all the required packages to your virtual environment to work with the project.

## Database setup

The first time you execute capstone, uncomment line 18 in app.py 
to create the database with a name of `capstone`, and all the necessary tables and relationships to work with the project. 
Be sure to comment again after the first run, or the database will be initialized.


## Data Modelling

The data model of the project is provided in `models.py` file in the root folder. 
The following schema for the database and helper methods are used for API behaviour:

- There are two tables created: Actors and Movies.
- The Actors table contains the name, age, and sex of the actors
- The Movies table contains the title and the release date of the movies.

To run the API server on a local development environmental the following commands must be additionally executed:

### On Linux: export
```
export FLASK_APP=app.py
export FLASK_ENV=development
```

### On Windows: set
```
set FLASK_APP=app.py
set FLASK_ENV=development
```

### API Server

All accessable endpoints of the project are located in the `app.py` file.

Run the following command in the project root folder to start the local development server:

```
flask run
```

## RBAC credentials and roles

Auth0 was set up to manage role-based access control for three users. The API documentation below describes, among others, 
by which user the endpoints can be accessed. Access credentials and permissions are handled with JWT tockens which must be 
included in the request header. 

### Permissions

Executive Producers can access API endpoints that have the following permission requirements:

    "delete:actors"	- delete an actor by actor_id
    "delete:movies"	- delete an actor by movie_id
    "get:actors"	- get a list of acrtors
    "get:movies"	- get a list of movies
    "patch:actors"	- update actors by actor_id
    "patch:movies"	- update movies by movie_id
    "post:actors"	- add actors
    "post:movies"	- add movies

Casting Director can access API endpoints that have the following permission requirements:

    "delete:actors"	- delete an actor by actor_id
    "get:actors"	- get a list of acrtors
    "get:movies"	- get a list of movies
    "patch:actors"	- update actors by actor_id
    "patch:movies"	- update movies by movie_id
    "post:actors"	- add actors

Casting Assistent can access API endpoints that have the following permission requirements:

    "get:actors"	- get a list of acrtors
    "get:movies"	- get a list of movies

## API endpoints

### Public endpoints
```
#### Post actors
- Adds an actor with the following form fields
- Form fields
	- name
	- age
	- sex
- Returns:  The actor added in json format, with a success flag and status_code
Sample response:
```
{
    "actors": {
        "age": "62",
        "gender": "Male",
        "id": 2,
        "name": "Sean Connery"
    },
    "status_code": 200,
    "success": true
}```
#### GET '/actors'
- Returns: The actors in json format

Sample response:
```
{
    "actors": [
        {
            "age": "68",
            "gender": "Male",
            "id": 1,
            "name": "Kevin Costner"
        },
        {
            "age": "62",
            "gender": "Male",
            "id": 2,
            "name": "Sean Connery"
        }
    ],
    "status_code": 200,
    "success": true
}
```
#### Patch '/actors/<int:actor_id>'
- Updates an actor by actor_id
- Form fields
	- name
	- age
	- sex
- Returns: The updated actor in json format, with a success flag and status_code
Sample response:
```
{
    "actors": {
        "age": "68",
        "gender": "Male",
        "id": 2,
        "name": "Sean Connery"
    },
    "status_code": 200,
    "success": true
}

```
#### Delete '/actors/<int:actor_id>'
- Deletes an actor by actor_id
- Returns: The success message in json format, with a status_code and actor_id deleted
Sample response:
```
{
    "actor_id": 1,
    "status_code": 200,
    "success": true
}
```
#### Post movies
- Adds an actor with the following forn fields
- Form fields
	- title
	- release_date
- Returns: The added movie in json format, with a success flag and status_code.
Sample response:
```
{
    "movies": {
        "release_date": "01/01/1990",
        "title": "Mad Movie 2"
    },
    "status_code": 200,
    "success": true
}
```
#### GET '/movies'
- Returns: The movies in json format, with a success flag and status_code.
Sample response:
```
{
    "movies": [
        {
            "id": 3,
            "release_date": "01/01/1990",
            "title": "Mad Movie 2"
        },
        {
            "id": 2,
            "release_date": "01/01/1986",
            "title": "Temple of Doom"
        }
    ],
    "status_code": 200,
    "success": true
}
```
#### Patch '/movies/<int:movie_id>'
- Updates an movie by movie_id
- Form fields
	- title
	- release_
- Returns: The movie updated in json format, with a success flag and status_code.
Sample response:
```
{
    "movies": {
        "id": 3,
        "release_date": "01/01/1990",
        "title": "Mad Movie 3"
    },
    "status_code": 200,
    "success": true
}
```
#### Delete '/movies/<int:movie_id>'
- Deletes an movie by movie_id
- Returns: A suuccess message in json format, along with a status_code and movie_id deleted.
Sample response:
```
{
    "movie_id": 3,
    "status_code": 200,
    "success": true
}
```
## Testing

The testing of all endpoints was implemented with unittest. Each endpoint can be tested with one success test case and one error test case. 
RBAC feature can also be tested for each type of user.

All test cases are stored in `first_test_app.py` and `second_test_app.py` files in the project rool folder.

Before running the test application, uncomment line 18 in testapp.py, and execute `python first_test_app.py`.  This job will intialize the database, 
and insert the necessary input records.  Next recomment the line 18 in testapp.py, and execute `python second_test_app.py` to run the test cases.

line 18  #db_drop_and_create_all()

```
## Heroku Deployment and Base URL

The backend application has been deployed on Heroku and can be accessed live at
```
https://capstone-kml.herokuapp.com/ 
```
