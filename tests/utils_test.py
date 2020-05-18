import unittest

from src.utils import generateBound, generateDirections
from helper import generateDirectionResp, generateDirectionEmptyResp

class UtilsTestCase(unittest.TestCase):

    def test_generate_bound(self):
        highestPos = { 'x': 3, 'y': 5 }
        lowestPos = { 'x': -2, 'y': -1 }
        expected = {
            "posXBound": [-2,-1,0,1,2,3],
            "posYBound": [5,4,3,2,1,0,-1]
        }
        res = generateBound(highestPos, lowestPos)
        self.assertEqual(res, expected)

    def test_generate_directions(self):
        path = '  LRFBE^ FR  '
        result = generateDirections(path)
        self.assertEqual(result, generateDirectionResp)

    def test_generate_directions_empty_path(self):
        path = ''
        result = generateDirections(path)
        self.assertEqual(result, generateDirectionEmptyResp)
    
    if __name__ == "__main__":
        unittest.main()
