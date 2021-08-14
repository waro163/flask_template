from flask import Flask, views, request
from flask_cors import CORS
# from flask.globals import request

app = Flask(__name__)
app.config.from_json("config.json")

cors = CORS()
cors.init_app(app=app)

# 基本函数方法
@app.route("/",methods=["GET","POST"])
def index():
    print(request.json)
    return app.config.get("RUN_ENV")

# url转换器
@app.route("/hello/<string:name>")
def hello(name):
    return "hello "+app.config.get("JWT_SECRET")

# 类视图
class HelloViews(views.MethodView):
    def get(self):
        return "hello view"

    def post(self):
        print(request.json)
        return "hello post view"

app.add_url_rule("/hi",view_func=HelloViews.as_view('hi'))

# 蓝图
from api_demo import api_bp
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run()