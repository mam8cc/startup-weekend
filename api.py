from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful_swagger import swagger
from resources.Backpack import Backpack as BackpackResource
from sqlalchemy.orm import relationship

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://eglwyuhzapnpqc:WCJteKjRmtakk5-_MHU4VRa-uj@ec2-54-204-43-139.compute-1.amazonaws.com:5432/d64ekjunetosea'
db = SQLAlchemy(app)
CORS(app)

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


api = swagger.docs(Api(app), apiVersion='0.1')
api.add_resource(BackpackResource, '/backpack')

if __name__ == '__main__':
    app.run(debug=True)
