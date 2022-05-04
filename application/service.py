from application.domain.recommendations import Recommendations
# from application.domain.recommendations import Restaurants
from application import db

# need to add restaurants functions too
from application.domain.restaurants import Restaurants


def add_new_recommendations(recommendation):
    db.session.add(recommendation)
    db.session.commit()


def get_all_recommendations():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Recommendations.query.all()


def get_recommendation_by_id(recommendation_id):
    if recommendation_id > 0:
        return Recommendations.query.get(recommendation_id)
    else:
        return None



# RESTAURANTS

def get_all_restaurants():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Restaurants.query.all()


def get_restaurant_by_id(restaurant_id):
    if restaurant_id > 0:
        return Restaurants.query.get(restaurant_id)
    else:
        return None


# 1st create functions in services.py
# 2nd updates routes function for get method + to include service.py function
# 3rd update jinja template

