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
    price = db.Column(db.Float)
    url = db.Column(db.String)
    url_img = db.Column(db.String)

    # color_id = db.Column(db.ForeignKey())
    # gender_id = db.Column(db.ForeignKey())
    # frame_type_id = db.Column(db.ForeignKey())
    # brand_id = db.Column(db.ForeignKey())

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'weight': fields.Integer,
        'volume': fields.Integer,
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

    backpack = relationship('Backpack', lazy='joined')

class Gear(db.Model):
    __tablename__ = 'gear'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    weight = db.Column(db.Float)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)

