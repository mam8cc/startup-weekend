from models.models import Category, Gear, GearPackageXref, Package
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

package = db_session.query(Package).filter(Package.name=="Day Hike").first()


gear = db_session.query(Gear).filter(Gear.name == "Platypus Hoser 2.0L Reservoir").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)

'''
gear = db_session.query(Gear).filter(Gear.name == "NEMO Hornet 2P Tent").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)


gear = db_session.query(Gear).filter(Gear.name == "Jetboil Sol Aluminum Companion Cup - 0.8 Liter").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)


gear = db_session.query(Gear).filter(Gear.name == "Snow Peak Titanium Spork").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)


gear = db_session.query(Gear).filter(Gear.name == "Petzl e+LITE Headlamp").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)


gear = db_session.query(Gear).filter(Gear.name == "REI Igneo Sleeping Bag").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)


gear = db_session.query(Gear).filter(Gear.name == "Therm-a-Rest Z Lite Sol Sleeping Pad").first()

gearPackageXref = GearPackageXref(
    gear = gear,
    package=package
)
db_session.add(gearPackageXref)
'''

db_session.commit()



