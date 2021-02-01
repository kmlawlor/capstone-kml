import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db, Actor, Movie
from auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# Init
'''
Uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
'''
# db_drop_and_create_all()

# ROUTES
'''
Implement the public get actors endpoint
'''


@app.route('/actors')
def retrieve_actors():
    current_actors = Actor.query.order_by(Actor.id).all()

    if len(current_actors) == 0:
        print("No actors")
        abort(404)

    print('Actors Retrieved:' + str(len(Actor.query.all())))
    actors = []
    for actor in current_actors:
        actors.append({
                        "id": actor.id,
                        "name": actor.name,
                        "age": actor.age,
                        "gender": actor.gender,
        })

    return jsonify({"success": True, "status_code": 200, "actors": actors})


'''
Implement create actor endpoint
'''


@app.route('/actors', methods=['POST'])
def create_actor():
    new_name = request.form.get('name')
    new_age = request.form.get('age')
    new_gender = request.form.get('gender')

    try:
        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        actor.insert()
        actors = {
                    "id": actor.id,
                    "name": actor.name,
                    "age": actor.age,
                    "gender": actor.gender,
        }

        return jsonify({"success": True, "status_code": 200, "actors": actors})

    except Exception as e:
        print(e)
        abort(422)


'''
Implement update actors endpoint
'''


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def actors_update(actor_id):
    try:
        new_name = request.form.get('name')
        new_age = request.form.get('age')
        new_gender = request.form.get('gender')

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(408)

        actor.name = new_name
        actor.age = new_age
        actor.gender = new_gender
        actor.update()
        actors = {
                    "id": actor_id,
                    "name": new_name,
                    "age": new_age,
                    "gender": new_gender,
        }

        return jsonify({"success": True, "status_code": 200, "actors": actors})

    except Exception as e:
        print(e)
        abort(408)


'''
Delete endpoint
'''


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    try:
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(408)

        actor.delete()

        return jsonify({"success": True, "status_code": 200,
                        "actor_id": actor_id})

    except Exception as e:
        print(e)
        abort(408)


'''
Implement the public get movies endpoint
'''


@app.route('/movies')
def retrieve_movies():
    current_movies = Movie.query.order_by(Movie.title).all()

    if len(current_movies) == 0:
        print("No movies")
        abort(414)

    print('Movies Retrieved:' + str(len(Movie.query.all())))
    movies = []
    for movie in current_movies:
        movies.append({
                        "id": movie.id,
                        "title": movie.title,
                        "release_date": movie.release_date,
        })

    return jsonify({"success": True, "status_code": 200, "movies": movies})


'''
Implement create movie endpoint
'''


@app.route('/movies', methods=['POST'])
def create_movie():
    new_title = request.form.get('title')
    new_release_date = request.form.get('release_date')

    try:
        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()
        movies = {
                    "title": new_title,
                    "release_date": new_release_date,
        }

        return jsonify({"success": True, "status_code": 200, "movies": movies})

    except Exception as e:
        print(e)
        abort(422)


'''
Implement update movies endpoint
'''


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def movies_update(movie_id):
    try:
        new_title = request.form.get('title')
        new_release_date = request.form.get('release_date')

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            print("No movies")
            abort(418)

        movie.title = new_title
        movie.release_date = new_release_date
        movie.update()
        movies = {
                    "id": movie_id,
                    "title": new_title,
                    "release_date": new_release_date,
        }

        return jsonify({"success": True, "status_code": 200, "movies": movies})

    except Exception as e:
        print(e)
        abort(418)


'''
Delete endpoint
'''


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    try:
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(418)

        movie.delete()

        return jsonify({"success": True, "status_code": 200,
                        "movie_id": movie_id})

    except Exception as e:
        print(e)
        abort(418)


# ERRORS


'''
Error handlers
'''


@app.errorhandler(422)
def unprocessable(error):
    print(error)
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def no_actors(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "actors not found"
    }), 404


@app.errorhandler(408)
def actor_not_found(error):
    print(error)
    return jsonify({
        "success": False,
        "error": 408,
        "message": "Specific actor not found"
    }), 408


@app.errorhandler(414)
def no_movies(error):
    return jsonify({
        "success": False,
        "error": 414,
        "message": "movies not found"
    }), 414


@app.errorhandler(418)
def movie_not_found(error):
    return jsonify({
        "success": False,
        "error": 418,
        "message": "Specific movie not found"
    }), 418


'''
Error handler for AuthError
'''


@app.errorhandler(401)
def handle_auth_error(ex):
    return jsonify({
        "success": False,
        "error": ex.code,
        "message": ex.description
    })
