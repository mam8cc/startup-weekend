from models.models import Color, BackpackColorXref, Backpack, Gender, FrameType, Brand, BackpackSize
from pip._vendor.distlib.compat import raw_input
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

print('Gender:  1=Men  2=Women 3=Unisex')
gender_input = raw_input('Gender: ')
if gender_input is '1':
    gender_input = 'Men'
elif gender_input is '2':
    gender_input = 'Women'
elif gender_input is '3':
    gender_input = 'Unisex'
else:
    exit()

print('Frame:  1=Internal  2=External 3=Frameless')
frame_input = raw_input('Frame: ')
if frame_input is '1':
    frame_input = 'Internal'
elif frame_input is '2':
    frame_input = 'External'
elif frame_input is '3':
    frame_input = 'Frameless'
else:
    exit()

print('**BACKPACK FIELDS**')
backpack_name = raw_input('Backpack Name: ')
price = raw_input('Price: $')
url = raw_input('Url: ')
print('**BACKPACK SPECS**')
size_name = raw_input('Size Name: ')
waist_low = raw_input('Waist Low: ')
waist_high = raw_input('Waist High: ')
torso_low = raw_input('Torso Low: ')
torso_high = raw_input('Torso High: ')
weight = raw_input('Weight(oz): ')
volume = raw_input('Volume(L): ')

brand_input = raw_input('Brand: ')

gender = db_session.query(Gender)\
    .filter(func.lower(Gender.name) == func.lower(gender_input))\
    .first()

brand = db_session.query(Brand)\
    .filter(func.lower(Brand.name) == func.lower(brand_input))\
    .first()

if brand is None:
    brand = Brand(
        name='brand_input'
    )
    db_session.add(brand)
    db_session.commit()

frame = db_session.query(FrameType)\
    .filter(func.lower(FrameType.name) == func.lower(frame_input))\
    .first()

backpack = Backpack(
    name=backpack_name,
    price=price,
    url=url,
    gender=gender,
    frame_type=frame,
    brand=brand
)
db_session.add(backpack)
db_session.commit()

while True:
    print('Color Loop, enter "quit" as the color to quit!')
    color_input = raw_input('Color: ')

    if color_input == 'quit':
        break

    image_url = raw_input('Image URL: ')

    color = db_session.query(Color)\
                .filter(func.lower(Color.name) == func.lower(color_input))\
                .first()

    if color is None:
        color = Color(
            name=color_input
        )
        db_session.add(color)
        db_session.commit()

    color_xref = BackpackColorXref(
        color=color,
        backpack=backpack,
        url_img=image_url
    )
    db_session.add(color_xref)
    db_session.commit()

print('Finished saving.  Exiting...')
