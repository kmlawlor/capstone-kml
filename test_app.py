import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import (
    setup_db,
    Actor,
    Movie
)


class CapstoneKMLTestCase(unittest.TestCase):
    '''This class represents the capstone-kml test case'''

    def setUp(self):
        '''Define test variables and initialize app.'''
        self.client = app.test_client
        pass
    
    def tearDown(self):
        pass

    def test_get_actors(self):
        """Test getting the actors """
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(data['error'], 404)

    def test_get_movies(self):
        """Test getting the movies """
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(data['error'], 414)

if __name__ == "__main__":
    unittest.main()
