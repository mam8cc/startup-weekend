from models.models import Category, Gear, GearCategoryXref, Backpack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

category = db_session.query(Category).filter(Category.name=="Water").first()

gear = Gear(
    name='Platypus Hoser 2.0L Reservoir',
    price=22.95,
    url='http://www.rei.com/product/767110/platypus-hoser-20l-reservoir-70-fl-oz',
    length=6,
    width=.1,
    height=16,
    weight=3.5,
    url_img='http://www.rei.com/zoom/ff/a039bf86-5091-4e57-bbd8-3ec399e3fa9b.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Platypus plusBottle 1-Liter Water Bottle with Push/Pull Cap',
    price=16.95,
    url='http://www.rei.com/product/768123/platypus-plusbottle-1-liter-water-bottle-with-pushpull-cap',
    length=6,
    width=.1,
    height=10.75,
    weight=0.8,
    url_img='http://www.rei.com/zoom/pp/54338cde-34d1-4563-921c-958025d61558.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

'''
Shelters
'''
category = db_session.query(Category).filter(Category.name=="Shelter").first()

gear = Gear(
    name='Big Agnes Fly Creek UL 2 Tent',
    price=349.95,
    url='http://www.rei.com/product/865393/big-agnes-fly-creek-ul-2-tent',
    length=18,
    width=4,
    height=4,
    weight=37,
    url_img='http://www.rei.com/zoom/jj/b27c3454-22e0-44b4-85c5-21d1626663a8.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='NEMO Hornet 2P Tent',
    price=365.95,
    url='http://www.rei.com/product/880476/nemo-hornet-2p-tent',
    length=19,
    width=5,
    height=5,
    weight=37,
    url_img='http://www.rei.com/zoom/vv/67206f3c-b3eb-42c7-82ee-d8c418778663.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)


'''
Kitchen
'''
category = db_session.query(Category).filter(Category.name=="Kitchen").first()

gear = Gear(
    name='Snow Peak Trek 900 Titanium Cookset',
    price=52.95,
    url='http://www.rei.com/product/768602/snow-peak-trek-900-titanium-cookset',
    length=5,
    width=5,
    height=5.5,
    weight=6,
    url_img='http://www.rei.com/zoom/dd/e025c1cc-90a3-46ee-a732-90b6f24fd7df.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Jetboil Sol Aluminum Companion Cup - 0.8 Liter',
    price=49.95,
    url='http://www.rei.com/product/813625/jetboil-sol-aluminum-companion-cup-08-liter',
    length=4.1,
    width=4.1,
    height=6.5,
    weight=7.7,
    url_img='http://www.rei.com/zoom/ff/c09a2c21-ea4a-47e4-9472-0dc850a0cddc.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='MSR WhisperLite International Backpacking Stove',
    price=99.95,
    url='http://www.rei.com/product/830341/msr-whisperlite-international-backpacking-stove',
    length=5.5,
    width=5,
    height=4,
    weight=10.9,
    url_img='http://www.rei.com/zoom/dd/e025c1cc-90a3-46ee-a732-90b6f24fd7df.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Snow Peak LiteMax Stove',
    price=59.95,
    url='http://www.rei.com/product/768603/snow-peak-litemax-stove',
    length=3,
    width=2.7,
    height=1.3,
    weight=1.9,
    url_img='http://www.rei.com/zoom/ww/0eb86a55-b138-479a-a4fe-febf5fc95837.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)

gear = Gear(
    name='Snow Peak Titanium Spork',
    price=8.95,
    url='http://www.rei.com/product/660002/snow-peak-titanium-spork',
    length=6.5,
    width=.1,
    height=1.625,
    weight=.6,
    url_img='http://www.rei.com/zoom/660002Lrg.jpg/440'
)
db_session.add(gear)

gearCategoryXref = GearCategoryXref(
    gear = gear,
    category=category
)
db_session.add(gearCategoryXref)


db_session.commit()