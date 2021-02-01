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
        """Define test variables and initialize app."""
        self.client = app.test_client
        pass

    def tearDown(self):
        """Define tear down."""
        pass

    def test_get_actors(self):
        """Test getting the actors """
        response = self.client().get('/actors')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_patch_actors(self):
        """Test updating the actors """
        fdata = {"name": "Kevin Costner", "age": "68", "gender": "Male"}
        response = self.client().patch('/actors/1',
                                       content_type='multipart/form-data',
                                       data=fdata)
        data = json.loads(response.data)

        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_get_actors_2(self):
        """Test getting the actors """
        response = self.client().get('/actors')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_delete_actors(self):
        """Test deleting the actors """
        response = self.client().delete('/actors/2')

        self.assertEqual(response.status_code, 200)

    def test_error_delete_actors(self):
        """Test deleting the actors """
        response = self.client().delete('/actors/99')

        self.assertEqual(response.status_code, 408)

    def test_get_final_actors(self):
        """Test getting the actors """
        response = self.client().get('/actors')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_get_movies(self):
        """Test getting the movies """
        response = self.client().get('/movies')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_patch_movies(self):
        """Test updating the movies """
        fdata = {"title": "Temple of Doom", "release_date": "01/01/1986"}
        response = self.client().patch('/movies/2',
                                       content_type='multipart/form-data',
                                       data=fdata)
        data = json.loads(response.data)

        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_get_movies_2(self):
        """Test getting the movies """
        response = self.client().get('/movies')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)

    def test_delete_movies(self):
        """Test deleting the movies """
        response = self.client().delete('/movies/1')

        self.assertEqual(response.status_code, 200)

    def test_error_delete_movies(self):
        """Test deleting the movies """
        response = self.client().delete('/movies/99')

        self.assertEqual(response.status_code, 418)

    def test_get_final_movies(self):
        """Test getting the movies """
        response = self.client().get('/movies')
        if (response.status_code != 200):
            print("API is not working. status code :" +
                  str(response.status_code))
        else:
            print("API is working. status code :" + str(response.status_code))
            data = json.loads(response.data)
            print(json.dumps(data, indent=4, sort_keys=True))

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
