from flask.ext.restful import fields
from flask.ext.restful_swagger import swagger
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Brand(db.Model):
    __tablename__ = 'brand'
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

@swagger.model
class Backpack(db.Model):

    __tablename__ = 'backpack'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    url = db.Column(db.String)
    colors = []

    gender_id = db.Column(db.ForeignKey("gender.id"))
    frame_type_id = db.Column(db.ForeignKey("frame_type.id"))
    brand_id = db.Column(db.ForeignKey("brand.id"))

    gender = relationship('Gender', foreign_keys=[gender_id])
    frame_type = relationship('FrameType', foreign_keys=[frame_type_id], lazy='joined')
    brand = relationship('Brand', foreign_keys=[brand_id], lazy='joined')


    gender_fields = {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name')
    }

    frame_fields = {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name')
    }

    brand_fields = {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name')
    }

    colors_fields = {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name')
    }

    colors_xref_fields = {
        'url_img': fields.String,
        'color': fields.Nested(colors_fields)
    }

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.Float,
        'url': fields.String,
        'gender': fields.Nested(gender_fields),
        'frame_type': fields.Nested(frame_fields),
        'brand': fields.Nested(brand_fields),
        'colors': fields.Nested(colors_xref_fields)
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

    url_img = db.Column(db.String)

    backpack_id = db.Column(db.ForeignKey('backpack.id'), primary_key=True)
    backpack = relationship('Backpack', foreign_keys=[backpack_id], lazy='joined')

    color_id = db.Column(db.ForeignKey('color.id'), primary_key=True)
    color = relationship('Color', foreign_keys=[color_id], lazy='joined')

    colors_fields = {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name')
    }

    resource_fields = {
        'url_image': fields.String,
        'color': fields.Nested(color)
    }

class Gear(db.Model):
    __tablename__ = 'gear'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    weight = db.Column(db.Float)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)

class Material(db.Model):
    __tablename__ = 'material'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Package(db.Model):
    __tablename__ = 'package'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GearMaterialXref(db.Model):
    __tablename__ = 'gear_material'

    gear_id = db.Column(db.ForeignKey('gear.id'), primary_key=True)
    gear = relationship('Gear', foreign_keys=[gear_id], lazy='joined')

    material_id = db.Column(db.ForeignKey('color.id'), primary_key=True)
    material = relationship('Color', foreign_keys=[material_id], lazy='joined')

class GearCategoryXref(db.Model):
    __tablename__ = 'gear_category'

    gear_id = db.Column(db.ForeignKey('gear.id'), primary_key=True)
    gear = relationship('Gear', foreign_keys=[gear_id], lazy='joined')

    category_id = db.Column(db.ForeignKey('color.id'), primary_key=True)
    category = relationship('Color', foreign_keys=[category_id], lazy='joined')

class GearPackageXref(db.Model):
    __tablename__ = 'gear_package'

    gear_id = db.Column(db.ForeignKey('gear.id'), primary_key=True)
    gear = relationship('Gear', foreign_keys=[gear_id], lazy='joined')

    package_id = db.Column(db.ForeignKey('color.id'), primary_key=True)
    package = relationship('Color', foreign_keys=[package_id], lazy='joined')

