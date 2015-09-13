from models.models import Category, Gear, GearCategoryXref, Backpack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

category = db_session.query(Category).filter(Category.name=="Sleeping Bags").first()

gear = Gear(
    name='REI Igneo Sleeping Bag',
    price=299.00,
    url='http://www.rei.com/product/862532/rei-igneo-sleeping-bag',
    length=18,
    width=8,
    height=8,
    weight=29,
    url_img='http://www.rei.com/zoom/vv/9ed38c11-b83f-48e3-9335-e92a204de451.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Mountain Hardwear Phantom 45 Sleeping Bag',
    price=330.00,
    url='http://www.rei.com/product/846739/mountain-hardwear-phantom-45-sleeping-bag',
    length=10,
    width=6,
    height=6,
    weight=20,
    url_img='http://www.rei.com/zoom/ss/a19f7a74-f2b1-44f0-875a-75e49ddf0a22.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

'''
Sleeping Pads
'''

category = db_session.query(Category).filter(Category.name=="Sleeping Pads").first()

gear = Gear(
    name='Therm-a-Rest Z Lite Sol Sleeping Pad',
    price=34.95,
    url='http://www.rei.com/product/829826/therm-a-rest-z-lite-sol-sleeping-pad',
    length=20,
    width=5.5,
    height=5,
    weight=14,
    url_img='http://www.rei.com/zoom/aa/2bf39799-b610-4946-ab86-092812693db2.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Therm-a-Rest NeoAir XLite Sleeping Pad',
    price=129.95,
    url='http://www.rei.com/product/881574/therm-a-rest-neoair-xlite-sleeping-pad',
    length=9,
    width=3.3,
    height=3.3,
    weight=16,
    url_img='http://www.rei.com/zoom/jj/a75ed224-d8e9-439d-9727-4f5458348ade.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

'''
Lighting
'''

category = db_session.query(Category).filter(Category.name=="Lighting").first()

gear = Gear(
    name='Petzl Zipka Headlamp',
    price=39.95,
    url='http://www.rei.com/product/892054/petzl-zipka-headlamp',
    length=2.5,
    width=2.25,
    height=1.5,
    weight=4.23,
    url_img='http://www.rei.com/zoom/ss/00706e8c-20b0-46e0-9c2a-80bbdc11f8e5.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Petzl e+LITE Headlamp',
    price=29.95,
    url='http://www.rei.com/product/838548/petzl-elite-headlamp',
    length=1.5,
    width=1.25,
    height=0.5,
    weight=0.95,
    url_img='http://www.rei.com/zoom/bb/937c375f-f5b1-4557-8da9-8d7edbe0c3ff.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

db_session.commit()



