import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, movie_actor
from auth import requires_auth, AuthError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello():
        return "Hello"

    '''
  Create an endpoint to handle GET requests for actors
  '''
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(f):
        actors = Actor.query.all()

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })

    '''
  Create an endpoint to handle GET requests for movies
  '''
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(f):
        movies = Movie.query.all()

        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        })

    '''
  Create an endpoint to handle DELETE requests for actors
  '''
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(f, id):
        actor = Actor.query.filter(id == Actor.id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                'success': True,
                'deleted_actor_id': id
            })

        except BaseException:
            abort(422)

    '''
  Create an endpoint to handle DELETE requests for movies
  '''
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(f, id):
        movie = Movie.query.filter(id == Movie.id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                'success': True,
                'deleted_movie_id': id
            })

        except BaseException:
            abort(422)

    '''
  Create an endpoint to handle PATCH requests for actors
  '''
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('modify:actors')
    def update_actor(f, id):
        actor = Actor.query.filter(id == Actor.id).one_or_none()

        if actor is None:
            abort(404)

        body = request.get_json()
        actor.name = body.get('name')
        actor.age = body.get('age')
        actor.gender = body.get('gender')

        try:
            actor.update()
            return jsonify({
                'success': True,
                'updated_actor_id': id,
                'actor': actor.format()
            })

        except BaseException:
            abort(422)

    '''
  Create an endpoint to handle PATCH requests for movies
  '''
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('modify:movies')
    def update_movie(f, id):
        movie = Movie.query.filter(id == Movie.id).one_or_none()

        if movie is None:
            abort(404)

        body = request.get_json()
        movie.title = body.get('title')
        movie.release_date = body.get('release_date')

        try:
            movie.update()
            return jsonify({
                'success': True,
                'updated_movie_id': id,
                'movie': movie.format()
            })

        except BaseException:
            abort(422)

    '''
  Create an endpoint to handle POST requests for actors
  '''
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_new_actor(f):
        body = request.get_json()
        actor_name = body.get('name')
        actor_age = body.get('age')
        actor_gender = body.get('gender')

        try:
            new_actor = Actor(
                name=actor_name,
                age=actor_age,
                gender=actor_gender)
            new_actor.insert()

            return jsonify({
                'success': True,
                'new_actor_id': new_actor.id,
                'new_actor': new_actor.format()
            })

        except BaseException:
            abort(422)

    '''
  Create an endpoint to handle POST requests for movies
  '''
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_new_movie(f):
        body = request.get_json()
        movie_title = body.get('title')
        movie_release_date = body.get('release_date')

        try:
            new_movie = Movie(
                title=movie_title,
                release_date=movie_release_date)
            new_movie.insert()

            return jsonify({
                'success': True,
                'new_movie_id': new_movie.id,
                'new_movie': new_movie.format()
            })

        except BaseException:
            abort(422)

    '''
  Create error handlers for expected errors
  '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': "resource not found",
            'error': 404
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'message': "unprocessable",
            'error': 422
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'message': "bad request",
            'error': 400
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': "method not allowed",
            'error': 405
        }), 405

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'message': "Unauthorized",
            'error': 401
        }), 401

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'message': error.status_code,
            'error': error.error['description']
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
