from functools import wraps
from flask import request,g
from flask import json
from flask.json import jsonify

class User:
    def __init__(self,name) -> None:
        self.name = name


def is_authenticated(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # 
        if request.json.get("name")=="waro" and request.json.get("passwd") == "123":
            g.user = User("waro")
            return f(*args,**kwargs)
        return jsonify(message="not auth"),401
    return decorated