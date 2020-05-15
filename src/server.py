import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def default():
    data = {
        'highestPosition': {
            'x': 5,
            'y': 2
        },
        'lowestPosition': {
            'x': -4,
            'y': 0
        }
    }
    return jsonify(data)


@app.errorhandler(404)
def notFound(e):
    data = {
        'status': 404,
        'message': 'The route you requested for was not found'
    }
    return jsonify(data)

app.run()
