from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize DB
db = SQLAlchemy(app)
# Initialize Marshmallow
ma = Marshmallow(app)

# Product Class/Model
# NOTE: If we want we can add diferent product categories as db relationships
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "qty")


# Initialize Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# NOTE: To initiliaze the db we have to open a python terminal the we write
#  "from app import db" the we usen the function "db.create_all()"

# Tutorial at https://youtu.be/PTZiDnuC86g?t=1207

# Run Server
if __name__ == "__main__":
    app.run(debug=True)
