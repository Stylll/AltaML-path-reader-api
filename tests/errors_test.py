import unittest

from src.errors import getMissingQueryError, getOsError, getServerError

class ErrorsTestCase(unittest.TestCase):

    def test_get_missing_query_error(self):
        expected = {
            "message": "filename is missing in the url query",
            "status": 400
        }
        res = getMissingQueryError()
        self.assertEqual(res, expected)

    def test_get_server_error(self):
        expected = {
            "message": "Internal Server Error",
            "status": 500
        }
        res = getServerError()
        self.assertEqual(res, expected)

    def test_get_os_error(self):
        expected = {
            "message": "An error occured while retrieving file or file doesn't exist",
            "status": 500
        }
        res = getOsError()
        self.assertEqual(res, expected)
    
    if __name__ == "__main__":
        unittest.main()
