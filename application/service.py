from application.domain.into_london import IntoLondon
from application.domain.local_events import LocalEvents
from application.domain.outdoor_activities import OutdoorActivities
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


# for places to eat page

# RESTAURANTS

def get_all_restaurants():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Restaurants.query.all()


def get_restaurant_by_id(restaurants_id):
    if restaurants_id > 0:
        return Restaurants.query.get(restaurants_id)

    return Restaurants.query.all()



# DATABASE FUNCTIONS FOR INTO THE CITY PAGE:

def get_all_city_events():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return IntoLondon.query.all()


def get_city_event_by_id(city_id):
    if city_id > 0:
        return IntoLondon.query.get(city_id)
    else:
        return None


# DATABASE FUNCTIONS FOR LOCAL EVENTS PAGE:

def get_all_local_events():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return LocalEvents.query.all()


def get_local_event_by_id(local_id):
    if local_id > 0:
        return LocalEvents.query.get(local_id)
    else:
        return None


# DATABASE FUNCTIONS FOR OUTDOOR ACTIVITIES:
def get_all_outdoor_activities():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return OutdoorActivities.query.all()


def get_outdoor_activity_by_id(outdoor_id):
    if outdoor_id > 0:
        return OutdoorActivities.query.get(outdoor_id)
    else:
        return None

# 1st create functions in services.py
# 2nd updates routes function for get method + to include service.py function
# 3rd update jinja template

