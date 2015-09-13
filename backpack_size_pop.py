from models.models import Color, BackpackColorXref, Backpack, Gender, FrameType, Brand, BackpackSize
from pip._vendor.distlib.compat import raw_input
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

print('**BACKPACK FIELDS**')
backpack_name = raw_input('Backpack Name: ')
backpack = db_session.query(Backpack)\
    .filter(func.lower(Backpack.name) == func.lower(backpack_name))\
    .first()

if backpack is None:
    exit()

while True:
    print('Size Loop, enter "quit" as the size name to quit!')
    size_name = raw_input('Size Name: ')

    if size_name == 'quit':
        break

    waist_low = raw_input('Waist Low: ')
    waist_high = raw_input('Waist High: ')
    torso_low = raw_input('Torso Low: ')
    torso_high = raw_input('Torso High: ')
    weight = raw_input('Weight(oz): ')
    volume = raw_input('Volume(L): ')

    size = BackpackSize(
        backpack=backpack,
        size_name=size_name,
        waist_range_high=waist_high,
        waist_range_low=waist_low,
        torso_range_high=torso_high,
        torso_range_low=torso_low,
        weight_oz=weight,
        volumn_liter=volume
    )
    db_session.add(size)
    db_session.commit()


print('Finished saving.  Exiting...')
