import os
import time
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from testapp import app
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
        response = self.client().get('/actors')

        self.assertEqual(response.status_code, 404)

    def test_get_movies(self):
        """Test getting the movies """
        response = self.client().get('/movies')

        self.assertEqual(response.status_code, 414)

    def test_post_actors(self):
        """Test adding an actor """
        fdata = {"name": "Kevin Costner", "age": "58", "gender": "Male"}
        res = self.client().post('/actors',
                                content_type='multipart/form-data',
                                data=fdata)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)


    def test_post_actors_2(self):
        """Test adding an actor """
        fdata = {"name": "Sean Connery", "age": "64", "gender": "Male"}
        res = self.client().post('/actors',
                                content_type='multipart/form-data',
                                data=fdata)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)


    def test_post_movies(self):
        """Test adding a movies """
        fdata = {"title": "Braveheart", "release_date": "01/01/1980"}
        res = self.client().post('/movies',
                                content_type='multipart/form-data',
                                data=fdata)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)

    def test_post_movies_2(self):
        """Test adding a movies """
        fdata = {"title": "Trmple of Doom", "release_date": "01/01/1982"}
        res = self.client().post('/movies',
                                content_type='multipart/form-data',
                                data=fdata)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)

if __name__ == "__main__":
    unittest.main()
