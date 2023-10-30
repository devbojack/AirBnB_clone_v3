#!/usr/bin/python3

"""
defines a route /status on the app_views Blueprint
which returns a JSON response with the status "OK" when accessed.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})
