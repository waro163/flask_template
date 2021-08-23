import click
from flask import Flask, views, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
# from sqlalchemy.ext.declarative import api
from exts import db,ma

app = Flask(__name__)
app.config.from_json("config.json")

# 跨域
cors = CORS()
cors.init_app(app=app)

# 数据库
db.init_app(app=app)
from api_demo.models import Book
migrate = Migrate(app, db)

# 序列器
ma.init_app(app)

# 添加flask自定义命令
# flask --help
# flask faked --fake (第2个是函数名称，第3个是选项)
@app.cli.command()
@click.option("--fake", is_flag=True, help="create fake data in database")
def faked(fake):
    if fake:
        click.confirm("create data for db,sure?", abort=True)
        data=[]
        from faker import Faker
        fake = Faker()
        for i in range(5):
            data.append(Book(name=fake.name(),authors=fake.user_name(),publish_date=fake.date(),price=fake.pyint(15,150),on_sale=fake.boolean(),publisher=fake.street_name()))
        db.session.add_all(data)
        db.session.commit()
        click.echo("all done")
    else:
        click.echo("good bye!")

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
    def get(self, *args, **kwargs):
        return jsonify({"args":args,
                        "kwargs":kwargs,
                        "request.args":request.args
                        })

    def post(self):
        print(request.json)
        return "hello post view"

app.add_url_rule("/hi/<string:name>",view_func=HelloViews.as_view('hi'))

# 蓝图
from api_demo import api_bp
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run()