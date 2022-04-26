from flask import Blueprint, render_template, jsonify

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    # return "<h1>Testing this home page route</h1>"
    return render_template("home.html")


@routes.route('/placestoeat')
def places_to_eat():
    return "<h1>Places to eat page </h1>"


@routes.route('/exploretheoutdoors')
def explore_the_outdoors():
    return "<h1>Explore the outdoors page</h1>"


@routes.route('/intothecitycentre')
def into_city_centre():
    return "<h1>Explore the city centre page</h1>"


@routes.route('/localevents')
def local_events():
    return "<h1>Explore the local events page</h1>"


@routes.route('/recommendations')
def recommendations():
    return "<h1>Recommendations Page</h1>"


@routes.route('/discounts')
def discounts():
    return "<h1>Discounts Page</h1>"





