import sqlalchemy
from sqlalchemy.orm import sessionmaker

from website.models.wrong import Restaurants

print(sqlalchemy.__version__)
from sqlalchemy import text


import pymysql
print(pymysql.__version__)


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@localhost/visiting_sky_db", echo=False, future=True)


with engine.connect() as conn:
    result = conn.execute(text("select * from restaurants"))
    for row in result:
        print(row)

#
# Session = sessionmaker(bind=engine)
#
# session = Session()
#
# restaurant = session.query(Restaurants).filter_by(id=2).first()
#
# print(restaurant)