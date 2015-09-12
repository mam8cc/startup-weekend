from flask.ext.restful import fields
from flask.ext.restful_swagger import swagger
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

@swagger.model
class Backpack(db.Model):

    __tablename__ = 'backpack'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    weight = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    price = db.Column(db.Integer)
    url = db.Column(db.String)

    # color_id = db.Column(db.ForeignKey())
    # gender_id = db.Column(db.ForeignKey())
    # frame_type_id = db.Column(db.ForeignKey())
    # brand_id = db.Column(db.ForeignKey())

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'weight': fields.Integer,
        'volume': fields.Integer,
        'price': fields.Integer,
        'url': fields.String
    }


class WaistDimension(db.Model):
    __tablename__ = 'dimension_waist'

    id = db.Column(db.Integer, primary_key=True)
    size_name = db.Column(db.String)
    size_range_low = db.Column(db.Integer)
    size_range_high = db.Column(db.Integer)

    backpack_id = db.Column(db.ForeignKey('backpack.id'))

    backpack = relationship('Backpack', lazy='joined')


class TorsoDimension(db.Model):
    __tablename__ = 'dimension_torso'

    id = db.Column(db.Integer, primary_key=True)
    size_name = db.Column(db.String)
    size_range_low = db.Column(db.Integer)
    size_range_high = db.Column(db.Integer)

    backpack_id = db.Column(db.ForeignKey('backpack.id'))
