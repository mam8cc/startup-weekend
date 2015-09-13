from flask.ext.restful import Resource, marshal_with
from models.models import Package, GearPackageXref, GearCategoryXref


class Packages(Resource):
    @marshal_with(Package.resource_fields)
    def get(self):
        return Package.query.all()

    @marshal_with(GearCategoryXref.resource_fields)
    def get(self, package_id):
        gear = GearPackageXref.query\
            .filter(GearPackageXref.package_id==package_id)\
            .all()

        package_gear = []

        for piece in gear:
            package_gear.append(piece.gear_id)

        gear_categories = GearCategoryXref.query\
            .filter(GearCategoryXref.gear_id.in_(package_gear))\
            .all()

        return gear_categories