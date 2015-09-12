from flask.ext.restful import fields
from flask.ext.restful_swagger import swagger
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

@swagger.model


class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class FrameType(db.Model):
    __tablename__ = 'frame_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Backpack(db.Model):

    __tablename__ = 'backpack'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    url = db.Column(db.String)
    url_img = db.Column(db.String)

    gender_id = db.Column(db.ForeignKey("gender.id"))
    frame_type_id = db.Column(db.ForeignKey("frametype.id"))
    brand_id = db.Column(db.ForeignKey("brand.id"))

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.Float,
        'url': fields.String,
        'url_img': fields.String
    }

class BackpackSize(db.Model):
    __tablename__ = 'backpack_size'

    id = db.Column(db.Integer, primary_key=True)
    size_name = db.Column(db.String)
    torso_range_low = db.Column(db.Float)
    torso_range_high = db.Column(db.Float)
    waist_range_low = db.Column(db.Float)
    waist_range_high = db.Column(db.Float)
    weight_oz = db.Column(db.Float)
    volumn_liter = db.Column(db.Integer)

    backpack_id = db.Column(db.ForeignKey('backpack.id'))

    backpack = relationship('Backpack', foreign_keys=[backpack_id], lazy='joined')

class BackpackColorXref(db.Model):
    __tablename__ = 'backpack_color'

    backpack_id = db.Column(db.ForeignKey('backpack.id'), primary_key=True)
    backpack = relationship('Backpack', lazy='joined')

    color_id = db.Column(db.ForeignKey('color.id'), primary_key=True)
    color = relationship('Color', lazy='joined')

class Gear(db.Model):
    __tablename__ = 'gear'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    weight = db.Column(db.Float)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)


