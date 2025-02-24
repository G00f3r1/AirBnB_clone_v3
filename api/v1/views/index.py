#!/usr/bin/python3
""" Index file """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """ Returns the API status """
    ret_status = {
        "status": "OK"
    }
    return jsonify(ret_status)


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def number_of_objects():
    """ Retrieves the number of each object by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
