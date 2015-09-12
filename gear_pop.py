from models.models import Category, Gear, GearCategoryXref, Backpack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))
categories = db_session.query(Category).filter(Category.name=="Food").all()
print(len(categories))

# category = print(Category.query.filter(Category.name == "Food"))
'''
gear = Gear(
    name='Mountain House: Chicken Breast and Mashed Potatoes',
    price=9.99,
    url='http://www.mountainhouse.com/M/product/chicken-breast.html?variant_id=38',
    length=6,
    width=2,
    height=7,
    weight=4.0
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Mountain House: Pasta Primavera',
    price=7.49,
    url='http://www.mountainhouse.com/M/product/pasta-primavera.html?variant_id=60',
    length=6,
    width=2,
    height=7,
    weight=5.0
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Mountain House: Sweet & Sour Pork with Rice',
    price=9.29,
    url='http://www.mountainhouse.com/M/product/sweet-sour-pork.html?variant_id=69',
    length=6,
    width=2,
    height=7,
    weight=6.0
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

db_session.commit() '''