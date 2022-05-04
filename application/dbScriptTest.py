import sqlalchemy
from sqlalchemy.orm import sessionmaker

from application.domain.recommendations import Recommendations
from application.domain.restaurants import Restaurants

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import text
import pymysql


engine = create_engine("mysql+pymysql://root:@localhost/visiting_sky_db", echo=False, future=True)
Session = sessionmaker(bind=engine)

session = Session()


print(sqlalchemy.__version__)
print(pymysql.__version__)


restaurant = session.query(Restaurants).filter_by(id=2).first()

print(restaurant.restaurant_name, restaurant.restaurant_address, restaurant.restaurant_location,
      restaurant.restaurant_website, restaurant.restaurant_description, restaurant.restaurant_cuisine_type,
      restaurant.restaurant_affordability)
#    # restaurant_image (to be added between restaurant_website and restaurant_description)


restaurant = session.query(Restaurants).filter_by(restaurant_name="Tiger Lily").first()
print(restaurant.restaurant_name, restaurant.restaurant_address, restaurant.restaurant_location,
      restaurant.restaurant_website, restaurant.restaurant_description, restaurant.restaurant_cuisine_type,
      restaurant.restaurant_affordability)
#     # restaurant_image (to be added between restaurant_website and restaurant_description)


recommendations = session.query(Recommendations).filter_by(recommendations_id=4).first()
print(recommendations.recommendation_location, recommendations.recommendation_discount)
for x in recommendations.recommendation_location:
    print(x.recommendation_name, x.recommendation_address)


# below displays content from our restaurants' table in sql (it works)
with engine.connect() as conn:
    result = conn.execute(text("select * from restaurants"))
    for row in result:
        print(row)





# martina's code:
# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()
