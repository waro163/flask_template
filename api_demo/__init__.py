from flask import Blueprint

# api_bp = Blueprint("api_demo",__name__,url_prefix="/api_demo")
api_bp = Blueprint("api_demo",__name__)

from . import views
api_bp.add_url_rule("login",view_func=views.LoginView.as_view("login"))
