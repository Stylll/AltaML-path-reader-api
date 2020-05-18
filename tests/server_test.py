import unittest
import json

from src.server import app
from helper import testResponseData

class ServerTestCase(unittest.TestCase):

    def test_directions(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/directions?filename=TEST-DO-NOT-UPDATE-DELETE', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        resp = json.loads(response.data)
        self.assertEqual(resp['data'], testResponseData)

    def test_directions_not_found(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/path', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        resp = json.loads(response.data)
        self.assertEqual(resp['message'], 'The route you requested for was not found')
        self.assertEqual(resp['status'], 404)

    def test_directions_filename_required(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/directions', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp = json.loads(response.data)
        self.assertEqual(resp['message'], 'filename is missing in the url query')
        self.assertEqual(resp['status'], 400)

    def test_directions_file_read_error(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/directions?filename=filename', content_type='application/json')
        self.assertEqual(response.status_code, 500)
        resp = json.loads(response.data)
        self.assertEqual(resp['message'], 'An error occured while retrieving file or file doesn\'t exist')
        self.assertEqual(resp['status'], 500)


    if __name__ == "__main__":
        unittest.main()
