from flask.ext.restful import Resource, marshal_with
from models.models import Package, GearPackageXref, Gear


class Packages(Resource):
    @marshal_with(Package.resource_fields)
    def get(self):
        return Package.query.all()

    @marshal_with(Gear.resource_fields)
    def get(self, package_id):
        gear = GearPackageXref.query\
                    .filter(GearPackageXref.package_id==package_id).all()

        package_gear = []

        for piece in gear:
            package_gear.append(piece.gear)

        return package_gear