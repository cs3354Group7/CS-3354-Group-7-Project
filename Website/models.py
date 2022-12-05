from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    __bind_key__ = 'three'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    mobile = db.Column(db.String(150))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))

class Inventory(db.Model):
    __bind_key__ = 'two'
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(150), unique = True)
    qty = db.Column(db.Integer)
    price = db.Column(db.Numeric(precision = 10, scale = 2), nullable = False)
    machine_id = db.Column(db.Integer)

class Money(db.Model):
    __bind_key__ = "four"
    id = db.Column(db.Integer, primary_key = True)
    machine = db.Column(db.String(150), unique = True)
    dollars = db.Column(db.Integer)
    quarters = db.Column(db.Integer)
    nickels = db.Column(db.Integer)
    dimes = db.Column(db.Integer)
    pennies = db.Column(db.Integer)
    total = db.Column(db.Numeric(precision = 10, scale = 2), nullable = False)

class Machines(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True)
    owner = db.Column(db.Integer)



