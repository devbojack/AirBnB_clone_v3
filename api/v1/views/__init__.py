#!/usr/bin/python3

"""
creates the app_views Blueprint with a URL
prefix of /api/v1. It also imports the views
you want to include in the blueprint.
"""

from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
