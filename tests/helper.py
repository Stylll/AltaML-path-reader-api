testResponseData = {
        "bound": {
            "posXBound": [-2,-1,0,1,2,3],
            "posYBound": [1,0,-1]
        },
        "endPosition": {
            "raw": [3,1],
            "string": "3/1"
        },
        "highestPosition": {"x": 3,"y": 1},
        "lastDirection": "up",
        "lowestPosition": {"x": -2,"y": -1},
        "multiOccurence": [],
        "path": {
            "raw": [
                [0,0],
                [0,1],
                [-1,1],
                [-2,1],
                [-2,0],
                [-2,-1],
                [-1,-1],
                [0,-1],
                [1,-1],
                [1,0],
                [2,0],
                [3,0],
                [3,1]
            ],
            "string": ["0/0","0/1","-1/1","-2/1","-2/0","-2/-1","-1/-1","0/-1","1/-1","1/0","2/0","3/0","3/1"]
        },
        "startPosition": {
            "raw": [0,0],
            "string": "0/0"
        }
    }

generateDirectionResp = {
        "bound": {
            "posXBound": [0],
            "posYBound": [2,1,0]
        },
        "endPosition": {
            "raw": [0,2],
            "string": "0/2"
        },
        "highestPosition": {"x": 0,"y": 2},
        "lastDirection": "right",
        "lowestPosition": {"x": 0,"y": 0},
        "multiOccurence": [],
        "path": {
            "raw": [
                [0,0],
                [0,1],
                [0,2],
            ],
            "string": ['0/0', '0/1', '0/2']
        },
        "startPosition": {
            "raw": [0,0],
            "string": "0/0"
        }
    }

generateDirectionEmptyResp = {
        "bound": {
            "posXBound": [0],
            "posYBound": [0]
        },
        "endPosition": {
            "raw": [0,0],
            "string": "0/0"
        },
        "highestPosition": {"x": 0,"y": 0},
        "lastDirection": "up",
        "lowestPosition": {"x": 0,"y": 0},
        "multiOccurence": [],
        "path": {
            "raw": [
                [0,0],
            ],
            "string": ['0/0']
        },
        "startPosition": {
            "raw": [0,0],
            "string": "0/0"
        }
    }
