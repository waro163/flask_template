from flask import Blueprint

# api_bp = Blueprint("api_demo",__name__,url_prefix="/api_demo")
api_bp = Blueprint("api_demo",__name__)

from .views import *
