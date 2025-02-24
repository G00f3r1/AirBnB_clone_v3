#!/usr/bin/python3
""" Starts a flask application """
from api.v1.views import app_views
from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from models import storage
from os import environ


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(exception):
    """ Calls storage.close() to close the database """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    host = environ.get("HBNB_API_HOST")
    port = environ.get("HBNB_API_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"

    app.run(host=host, port=port, threaded=True, debug=True)
