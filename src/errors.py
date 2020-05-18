def getMissingQueryError():
    return {
        "message": "filename is missing in the url query",
        "status": 400
    }

def getServerError():
    return {
        "message": "Internal Server Error",
        "status": 500
    }

def getOsError():
    return {
        "message": "An error occured while retrieving file or file doesn't exist",
        "status": 500
    }
