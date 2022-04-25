import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import text


import pymysql
print(pymysql.__version__)


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@localhost/visiting_sky", echo=False, future=True)


with engine.connect() as conn:
    result = conn.execute(text("select * from restaurants"))
    for row in result:
        print(row)

