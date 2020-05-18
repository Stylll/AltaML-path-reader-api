import flask

from flask import jsonify, request
from flask_cors import CORS
from src.errors import getMissingQueryError, getServerError, getOsError
from src.utils import readFile, generateDirections

app = flask.Flask(__name__)
CORS(app)
# app.config['DEBUG'] = True

@app.route('/api/v1/directions', methods=['GET'])
def directions():

    #get file name from url
    queryName = 'filename'
    if queryName not in request.args:
        return jsonify(getMissingQueryError()), 400

    filename = request.args[queryName]

    try:
        pathStr = readFile(filename)
        pathStr = pathStr.strip()

        generatedDirections = generateDirections(pathStr)
        data = {
            'data': generatedDirections,
            'status': 200
        }

        return jsonify(data), 200

    except OSError:
        return jsonify(getOsError()), 500
    except Exception: #pylint: disable=broad-except
        return jsonify(getServerError()), 500


#pylint: disable=unused-argument
@app.errorhandler(404)
def notFound(e):
    data = {
        'status': 404,
        'message': 'The route you requested for was not found'
    }
    return jsonify(data), 404

@app.errorhandler(500)
def serverError(e):
    data = {
        'status': 500,
        'message': 'Internal Server Error'
    }
    return jsonify(data), 500
