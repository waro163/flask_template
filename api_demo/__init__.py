from flask import Blueprint, request, views

api_bp = Blueprint("api_demo",__name__,url_prefix="/api_demo")

from .views import *
