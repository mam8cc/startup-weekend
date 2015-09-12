from models.models import Category, Gear
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

engine = create_engine('postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21')
db_session = scoped_session(sessionmaker(bind=engine))

category = Category(
    name='Food'
)
db_session.add(category)

category = Category(
    name='Shelter'
)
db_session.add(category)

category = Category(
    name='Clothing'
)
db_session.add(category)

category = Category(
    name='Kitchen'
)
db_session.add(category)

category = Category(
    name='First Aid'
)
db_session.add(category)

category = Category(
    name='Tools'
)
db_session.add(category)

category = Category(
    name='Sleeping Bags'
)
db_session.add(category)

category = Category(
    name='Sleeping Pads'
)
db_session.add(category)

category = Category(
    name='Lighting'
)
db_session.add(category)

category = Category(
    name='Tools'
)
db_session.add(category)

category = Category(
    name='Trekking Poles'
)
db_session.add(category)

category = Category(
    name='Toiletries'
)
db_session.add(category)

category = Category(
    name='Electronics'
)
db_session.add(category)

category = Category(
    name='Organization'
)
db_session.add(category)
db_session.commit()
