#!/usr/bin/python3

"""
defines a route /status on the app_views Blueprint
which returns a JSON response with the status "OK" when accessed.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    stats_dict = {}
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    for cls in classes:
        count = storage.count(cls)
        stats_dict[cls] = count

    return jsonify(stats_dict)
