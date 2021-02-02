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

Before running the test application, uncomment line 18 in app.py, and execute `python first_test_app.py`.  This job will intialize the database, 
and insert the necessary input records.  Next recomment the line 18 in app.py, and execute `python second_test_app.py` to run the test cases.

line 18  #db_drop_and_create_all()

```
## Heroku Deployment and Base URL

The backend application has been deployed on Heroku and can be accessed live at
```
https://capstone-kml.herokuapp.com/ 

Tokens:
Executive Producer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVZS1doQy1ZSmZWWUFoTVFtOWtiRiJ9.eyJpc3MiOiJodHRwczovL2ttbC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkMjcwZDA5ODgwNDkwMDcxNjFkMGMzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MTIxOTEyNTMsImV4cCI6MTYxMjI3NzY1MywiYXpwIjoiZHJsa3JDVjNVWDZFUXlydzVWZGU1elh1SE5MQ0dMa3IiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.hyBW2qjjPzhEhf1idQoyCk1ySd03eWgvTsCV8yfK9XD6_rY-hNmJry1xng6OVB8p5IJ6BoYwBXm5W0z0uDJMJ3fmTn5aEI9huZZqCNJYzpyfR63fC3zpwGXD1up9xSA1uV03yHD5fwnh4uRQeG7Q87ePAtG1wuBMamW-w4-f-LodisJvgo7iF1AdgkiRWTCy6eA2Z5UGhQlfQhx2PmYhesyXGyPjtd-KA0uvAUcs7TdfXczVY8Hwxt6W4pap3xq_QSPFLsKU5OvKbXIhbLLoWSOqTPNc8JdwsJvDgoMhgfUiBNtYkmaLfwQwWSxvlMr9XvyhmPFwBtyzFOSMHX9KHw

Casting Director
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVZS1doQy1ZSmZWWUFoTVFtOWtiRiJ9.eyJpc3MiOiJodHRwczovL2ttbC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkMjcwZDA5ODgwNDkwMDcxNjFkMGMzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MTIyMjI5OTMsImV4cCI6MTYxMjMwOTM5MywiYXpwIjoiZHJsa3JDVjNVWDZFUXlydzVWZGU1elh1SE5MQ0dMa3IiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.GxOIrx6halZUFA2-ffNtg3Z7BVFZOajrja-tUgP1dqTOY-XJjQ6zJBLrBYe00_lEm_Q-ueBXPSMzdw-rcMlVRS00bbZA8kNpC-aQZ6X82RNQ39V_r8oDvqB_7UggY2BC77IQvOVjFntaKPAzbxW9Ldu6_T-fDMjx6RfhePZMA_WhWauDIe4T05twTgul6DlAHz--JfAiX9u0sZDN1E0C90uBVexmSlJckDNoiBJBDjbeQAPpf0I7aqYxdNmrYHhU7gvrXOVk6u3Wq21u7h-68DCfwtLyFLc_BkNjgEJlqQO9eJiV6dxUiwehX_IxG-F74rjO3WZmw5pKaLPqHF45GA

Casting Assistaqnt
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVZS1doQy1ZSmZWWUFoTVFtOWtiRiJ9.eyJpc3MiOiJodHRwczovL2ttbC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkMjcwZDA5ODgwNDkwMDcxNjFkMGMzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MTIyMjQ4NDcsImV4cCI6MTYxMjMxMTI0NywiYXpwIjoiZHJsa3JDVjNVWDZFUXlydzVWZGU1elh1SE5MQ0dMa3IiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.LrXhL-rmUQyty27CMCaoL174mrdMdA07D_NFtWTiWIF9TN9cKQaEFKJSNTfb8fXb6__TAQLxHWwJNQNhDVlzviDFX0XHAqxlkh8FpSzwD_FHRVATpX2qggfh47jVHQh_VdD4J9jUPCIRctDRnFl0aElSY7_pAvbgvZjqWCjwkbrBwFKUSN87bVXMgTR0kSeysltp0Zs0WRSoyqFI1nXdlUVE4Gj_UHDb4-ydOnLE8WwHF7CKOQ1irmSui-pPrcUjfxtEdyb0zUw4ZoUWCfpbUqrIZ9JPpIhBTpK3RiPGih4_39X8s7Ww6IK-yNZvREE7SLW8WpaWYQUT8woTzGWzPw