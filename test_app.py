import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import (
    setup_db,
    Actor,
    Movie
)


class CapstoneKMLTestCase(unittest.TestCase):
    '''This class represents the capstone-kml test case'''

    def setUp(self):
        '''Define test variables and initialize app.'''
        pass
    
    def tearDown(self):
        pass

    def test_get_actors(self):
        """Test getting the actors """
        res = self('/actors')

        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
