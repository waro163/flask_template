from exts import ma
from marshmallow import fields

class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "authors", "publish_date", "price", "on_sale", "publisher")

class NewBookSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    authors = fields.String()
    publish_date = fields.Date()
    price = fields.Float()
    on_sale = fields.Boolean()
    # publisher = fields.String()

# book_schema = BookSchema()
# books_schema = BookSchema(many=True)
book_schema = NewBookSchema()
books_schema = NewBookSchema(many=True)
