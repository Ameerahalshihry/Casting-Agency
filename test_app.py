import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.assistant_token = os.environ['assistant_token']
        self.director_token = os.environ['director_token']
        self.producer_token = os.environ['producer_token']
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'michle',
            'age': 33,
            'gender': 'male'
            }
        self.new_movie = {
            'title': 'Mirror',
            'release_date': '2021/10/10'
            }
        
    def tearDown(self):
        """Executed after reach test"""
        pass  

    '''
    A C T O R 
    '''
    """
    Test GET endpoint
    """
    # def test_home(self):
    #     res = self.client().get('/')

    #     self.assertEqual(res.status_code, 200)

    # def test_get_actors_without_token(self):
    #     res = self.client().get('/actors')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 401)
    #     self.assertEqual(data['error'], 'Authorization header is expected.')

    # def test_get_actors_with_valid_token(self):
    #     res = self.client().get('/actors', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['actors']))
    '''
    Test DELETE endpint
    '''
    # def test_delete_actors(self):
    #     res = self.client().delete('/actors/2', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted_actor_id'], 2)

    # def test_404_delete_if_actors_does_not_exist(self):
    #     res = self.client().delete('/actors/1010', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_403_delete_actors_from_user_not_allowed(self):
    #     res = self.client().delete('/actors/3', headers={'Authorization': "Bearer {}".format(self.assistant_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')
    '''
    Test PATCH endpoint
    '''
    # def test_patch_actors(self):
    #     res = self.client().patch('/actors/3', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)},
    #         json={'name':'Sam', 'age':30, 'gender': 'male'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['updated_actor_id'], 3)
    #     self.assertTrue(len(data['actor']))

    # def test_404_patch_if_actors_does_not_exist(self):
    #     res = self.client().patch('/actors/99', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)}, 
    #         json={'name':'Sam', 'age':30, 'gender': 'male'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_403_patch_actors_from_user_not_allowed(self):
    #     res = self.client().patch('/actors/3', 
    #         headers={'Authorization': "Bearer {}".format(self.assistant_token)},
    #         json={'name':'Sam', 'age':30, 'gender': 'male'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')
    '''
    Test POST endpoint
    '''
    # def test_post_actors(self):
    #     res = self.client().post('/actors', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)},
    #         json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertIn('new_actor_id', data)
    #     self.assertTrue(len(data['new_actor']))

    # def test_422_post_invalid_actor(self):
    #     res = self.client().post('/actors', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)}, 
    #         json={'age':50, 'gender': 'male'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    # def test_403_post_actors_from_user_not_allowed(self):
    #     res = self.client().post('/actors', 
    #         headers={'Authorization': "Bearer {}".format(self.assistant_token)},
    #         json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')

    '''
    M O V I E
    '''
    """
    Test GET endpoint
    """
    # def test_get_movies_without_token(self):
    #     res = self.client().get('/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 401)
    #     self.assertEqual(data['error'], 'Authorization header is expected.')

    # def test_get_movies_with_valid_token(self):
    #     res = self.client().get('/movies', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['movies']))
    '''
    Test DELETE endpint
    '''
    # def test_delete_movies(self):
    #     res = self.client().delete('/movies/1', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted_movie_id'], 1)

    # def test_404_delete_if_movies_does_not_exist(self):
    #     res = self.client().delete('/movies/1000', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_403_delete_movies_from_user_not_allowed_assistant(self):
    #     res = self.client().delete('/movies/3', headers={'Authorization': "Bearer {}".format(self.assistant_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')

    # def test_403_delete_movies_from_user_not_allowed_director(self):
    #     res = self.client().delete('/movies/3', headers={'Authorization': "Bearer {}".format(self.director_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')
    '''
    Test PATCH endpoint
    '''
    # def test_patch_movies_from_producer(self):
    #     res = self.client().patch('/movies/3', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)},
    #         json={'title':'The Happiest Story', 'release_date': '2021/10/10'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['updated_movie_id'], 3)
    #     self.assertTrue(len(data['movie']))

    # def test_patch_movies_from_director(self):
    #     res = self.client().patch('/movies/3', 
    #         headers={'Authorization': "Bearer {}".format(self.director_token)},
    #         json={'title':'The Happiest Story Ever', 'release_date': '2022/10/10'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['updated_movie_id'], 3)
    #     self.assertTrue(len(data['movie']))

    # def test_404_patch_if_movies_does_not_exist(self):
    #     res = self.client().patch('/movies/99', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)}, 
    #         json={'title':'The Happiest Story Ever', 'release_date': '2022/10/10'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_403_patch_movies_from_user_not_allowed(self):
    #     res = self.client().patch('/movies/3', 
    #         headers={'Authorization': "Bearer {}".format(self.assistant_token)},
    #         json={'title':'The Happiest Story Ever', 'release_date': '2022/10/10'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')
    '''
    Test POST endpoint
    '''
    # def test_post_movies(self):
    #     res = self.client().post('/movies', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)},
    #         json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertIn('new_movie_id', data)
    #     self.assertTrue(len(data['new_movie']))

    # def test_422_post_invalid_movie(self):
    #     res = self.client().post('/movies', 
    #         headers={'Authorization': "Bearer {}".format(self.producer_token)}, 
    #         json={'title':'The Hope'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    # def test_403_post_movies_from_user_not_allowed_assistant(self):
    #     res = self.client().post('/movies', 
    #         headers={'Authorization': "Bearer {}".format(self.assistant_token)},
    #         json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')

    # def test_403_post_movies_from_user_not_allowed_director(self):
    #     res = self.client().post('/movies', 
    #         headers={'Authorization': "Bearer {}".format(self.director_token)},
    #         json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 403)
    #     self.assertEqual(data['error'], 'Permission not found.')


if __name__ == "__main__":
    unittest.main()