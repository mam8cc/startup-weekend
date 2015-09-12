from models.models import Color, BackpackColorXref, Backpack, Gender, FrameType, Brand
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

gender = Gender(
    name='M'
)
db_session.add(gender)
db_session.commit()

frame_type = FrameType(
    name='internal'
)
db_session.add(frame_type)
db_session.commit()

brand = Brand(
    name='Patagonia'
)
db_session.add(brand)
db_session.commit()

backpack = Backpack(
    name='PATAGONIA ASCENSIONIST PACK 45L',
    price=179,
    url='http://www.patagonia.com/us/product/ascensionist-pack-45-liters?p=48000-0',
    gender=gender,
    frame_type=frame_type,
    brand=brand
)

db_session.add(backpack)
db_session.commit()

color = Color(name='Chartreuse')
db_session.add(color)
db_session.commit()

backpackColor = BackpackColorXref(
    color=color,
    url_image='http://www.patagonia.com/tsimages/48000_CHRT.fpx?wid=750&hei=750&bgcolor=FFFFFF&ftr=6&cvt=jpeg,scans=progressive',
    backpack=backpack
)
db_session.add(backpackColor)
db_session.commit()
