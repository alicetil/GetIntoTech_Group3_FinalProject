import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import text

#from sqlalchemy.orm import sessionmaker

import pymysql
print(pymysql.__version__)


from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:@localhost/visiting_sky_db', echo=False, future=True)
#Session = sessionmaker(bind=engine)

#session = Session()

with engine.connect() as conn:
    result = conn.execute(text("select * from restaurants"))
    for row in result:
        print(row)

