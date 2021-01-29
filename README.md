# Capstone-kml

## Description

This project demonstrates what we have learned in the Udacity Full Stack Web Developer nano degree course.  It enables users to create, view, update and delete actors and movies.  The backend is designed to work for three types of users: Casting Assistant, Casting Director, and Executive Producers. 

Executive Producers are super users, and can create, view, update and delete actors and movies.  A Casting Assistant can only view actors and mocies.  Casting Director can create, view, update and delete actors, but can only view or update movies. Users must be authorized to be able to perform role-based requests to the backend via API described below. 

Authorization of users is enabled via Auth0 in which two seperate roles (companies and candidates) have been created and assigned seperate permissions. 

## Project dependencies

The project depends on the latest version of Python 3.x which we recommend to download and install from their official website and use a virtual environment to install all dependencies.

## PIP dependencies

After having successfully installed Python, navigate to the root folder of the project (the project must be forked to your local machine) and run the following in a command line:

```
pip3 install -r requirements.txt
```

This will install all the required packages to your virtual environment to work with the project.

## Database setup

The first time you execute capstone, uncomment line 18 in app.py 
to create the database with a name of `capstone`, and all the necessary tables and relationships to work with the project. Be sure to comment again after the first run, or the database will be initialized.


## Data Modelling

The data model of the project is provided in `models.py` file in the root folder. The following schema for the database and helper methods are used for API behaviour:

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

Auth0 was set up to manage role-based access control for three users. The API documentation below describes, among others, by which user the endpoints can be accessed. Access credentials and permissions are handled with JWT tockens which must be included in the request header. 

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
- Adds an actor with the following forn fields
- Form fields
	- name
	- age
	- sex
- Returns:  a text field withe the added name

Sample response:
```
Kevin Costner added.
```
#### GET '/actors'
- Returns: A html table with actors

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Age</th>
		<th>Gender</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Persaon1</td>
		<td>36</td>
		<td>Female</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Persaon2</td>
		<td>24</td>
		<td>Female</td>
	</tr>
</table>

```
#### Patch '/actors/<int:actor_id>'
- Updates an actor by actor_id
- Form fields
	- name
	- age
	- sex
- Returns: A html table with all actors including the updated actor

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Age</th>
		<th>Gender</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Persaon1</td>
		<td>36</td>
		<td>Female</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Persaon2</td>
		<td>24</td>
		<td>Female</td>
	</tr>
</table>
```

```
#### Delete '/actors/<int:actor_id>'
- Deletes an actor by actor_id
- Returns: A html table with all actors remaining

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Age</th>
		<th>Gender</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Persaon1</td>
		<td>36</td>
		<td>Female</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Persaon2</td>
		<td>24</td>
		<td>Female</td>
	</tr>
</table>
```
#### Post movies
- Adds an actor with the following forn fields
- Form fields
	- title
	- release_date
- Returns:  a text field withe the added title

Sample response:
```
Braveheart added
```
#### GET '/movies'
- Returns: A html table with movies

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Title</th>
		<th>Date</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Tremors</td>
		<td>01/01/1980</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Tremors 2</td>
		<td>01/01/1982</td>
	</tr>
	<tr>
		<td>3</td>
		<td>Tremors 3</td>
		<td>01/01/1988</td>
	</tr>
</table>
S
#### Patch '/movies/<int:movie_id>'
- Updates an movie by movie_id
- Form fields
	- title
	- release_
- Returns: A html table with all movies including the updated movie

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Title</th>
		<th>Date</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Tremors</td>
		<td>01/01/1980</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Tremors 2</td>
		<td>01/01/1984</td>
	</tr>
	<tr>
		<td>3</td>
		<td>Tremors 3</td>
		<td>01/01/1988</td>
	</tr>
</table>```

```
#### Delete '/movies/<int:movie_id>'
- Deletes an movie by movie_id
- Returns: A html table with all movies remaining

Sample response:
```
<table>
	<tr>
		<th>ID</th>
		<th>Title</th>
		<th>Date</th>
	</tr>
	<tr>
		<td>1</td>
		<td>Tremors</td>
		<td>01/01/1980</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Tremors 2</td>
		<td>01/01/1982</td>
	</tr>
</table>>

## Testing

The testing of all endpoints was implemented with unittest. Each endpoint can be tested with one success test case and one error test case. RBAC feature can also be tested for each type of user.

All test cases are soted in `test_app.py` file in the project rool folder.

Before running the test application, uncomment line 18 in app.py.  Then recomment the line and run the test cases.

#db_drop_and_create_all()

```

Then in the command line interface run the test file:

`python3 test_app.py`

## Heroku Deployment and Base URL

The backend application has been deployed on Heroku and can be accessed live at
```
https://capstone-kml.herokuapp.com/ 
```
