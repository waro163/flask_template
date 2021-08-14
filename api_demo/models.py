from exts import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    authors = db.Column(db.String(32))
    publish_date = db.Column(db.Date())
    price = db.Column(db.Float)
    on_sale = db.Column(db.Boolean, default=True)
    publisher = db.Column(db.String(64))