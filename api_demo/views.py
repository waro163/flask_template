from flask import request, views
from flask import json
from flask.helpers import make_response
from flask.json import jsonify
from flask_sqlalchemy import Pagination
from . import api_bp
from .pagination import BasePagination
from .permission import is_authenticated
from .models import Book

class LoginView(views.MethodView):

    # decorators = [is_authenticated]

    def get(self):
        pagination = BasePagination(Book.query)
        return jsonify(pagination.to_json())
        # return jsonify(message="welcome login")

    def post(self):
        name, passwd = request.json.get("name"), request.json.get("passwd")
        if name=="waro" and passwd == "123456":
            response = make_response(json.dumps({"name":name}))
            response.mimetype = "application/json"
            response.status_code = 201
            return response
        return jsonify(message="bad reqeust"),400

api_bp.add_url_rule("login",view_func=LoginView.as_view("login"))

