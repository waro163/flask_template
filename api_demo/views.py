from flask import request, views
from flask import json
from flask.helpers import make_response
from flask.json import jsonify
from . import api_bp
from .permission import is_authenticated

class LoginView(views.MethodView):

    decorators = [is_authenticated]

    def get(self):
        return jsonify(message="welcome login")

    def post(self):
        name, passwd = request.json.get("name"), request.json.get("passwd")
        if name=="waro" and passwd == "123456":
            response = make_response(json.dumps({"name":name}))
            response.mimetype = "application/json"
            response.status_code = 201
            return response
        return jsonify(message="bad reqeust"),400

api_bp.add_url_rule("login",view_func=LoginView.as_view("login"))