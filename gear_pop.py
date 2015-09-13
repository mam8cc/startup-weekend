from models.models import Category, Gear, GearCategoryXref, Material, GearMaterialXref, Package, GearPackageXref
from pip._vendor.distlib.compat import raw_input
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

category_input = raw_input('Category: ')
category = db_session.query(Category).filter(func.lower(Category.name) == func.lower(category_input)).first()

if category is None:
    category = Category(
        name=category_input
    )
    db_session.add(category)
    db_session.commit()

material_input = raw_input('Material: ')
material = db_session.query(Material).filter(func.lower(Material.name) == func.lower(material_input)).first()

if material is None:
    material = Material(
        name=material_input
    )
    db_session.add(material)
    db_session.commit()

print('***GEAR DATA***')
name = raw_input('Name: ')
price = raw_input('Price: $')
url = raw_input('Url: ')
url_img = raw_input('Url Image: ')
length = raw_input('Length: ')
width = raw_input('Width: ')
height = raw_input('Height: ')
weight = raw_input('Weight: ')

gear = Gear(
    name=name,
    price=price,
    url=url,
    url_img=url_img,
    length=length,
    width=width,
    height=height,
    weight=weight
)

db_session.add(gear)
db_session.commit()

materialXref = GearMaterialXref(
    material=material,
    gear=gear
)

categoryXref = GearCategoryXref(
    category=category,
    gear=gear
)

db_session.add(materialXref)
db_session.add(categoryXref)
db_session.commit()

packages = db_session.query(Package).all()

print('Add it to which package:')
for package in packages:
    print(str(package.id) + ' ' + package.name)

package_selection = raw_input('Package: ')

package = db_session.query(Package).get(package_selection)

packageXref = GearPackageXref(
    package=package,
    gear=gear
)
db_session.add(packageXref)
db_session.commit()

print('Done!  Exiting...')