from application.domain import restaurants
from application.domain.into_london import into_london
from application.domain.local_events import local_events
from application.domain.outdoor_activities import outdoor_activities
from application.domain.recommendations import Recommendations
# from application.domain.recommendations import Restaurants
from application import db

# need to add restaurants functions too


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

# places to eat page

def get_all_restaurants():
    return restaurants.query.all()

def get_restaurant_by_id(restaurants_id):
    if restaurants_id > 0:
        return restaurants.query.get(restaurants_id)
    else:
        return None

#Database Functions for Into the City

def get_all_city_events():
    return into_london.query.all()

def get_city_by_id(city_id):
    if city_id >0:
        return into_london.query.get(city_id)
    else:
        return None

# Database Functions for Local Events

def get_all_local_events():
    return local_events.query.all()

def get_local_event_by_id(local_id):
    if local_id > 0:
        return local_events.query.get(local_id)
    else:
        return None

# Database Function for Outdoor Activities

def get_all_outdoor_activities():
    return outdoor_activities.query.all()

def get_outdoor_activity_by_id(outdoor_id):
    if outdoor_id >0:
        return outdoor_activities.query.get(outdoor_id)
    else:
        return None

