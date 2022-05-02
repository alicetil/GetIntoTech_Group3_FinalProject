from flask import Blueprint, render_template, jsonify, request

from website import service
from website.domain.recommendations import Recommendations
from website.forms.recommendationsForm import RecommendForm

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    # return "<h1>Testing this home page route</h1>"
    return render_template("home.html")


@routes.route('/placestoeat')
def places_to_eat():
    # return "<h1>Places to eat page </h1>"
    return render_template("placestoeat.html")


@routes.route('/exploretheoutdoors')
def explore_the_outdoors():
    # return "<h1>Explore the outdoors page</h1>"
    return render_template("exploretheoutdoors.html")



@routes.route('/intothecitycentre')
def into_city_centre():
    # return "<h1>Explore the city centre page</h1>"
    return render_template("intothecitycentre.html")


@routes.route('/localevents')
def local_events():
    # return "<h1>Explore the local events page</h1>"
    return render_template("localevents.html")


# @routes.route('/recommendations')
# def recommendations():
#     # return "<h1>Recommendations Page</h1>"
#     return render_template("recommendations.html")

@routes.route('/recommendations', methods=['GET','POST'])
def add_recommendations():
    # global recommendations
    error = ""
    form = RecommendForm()

    if request.method == "POST":
        form = RecommendForm(request.form)
        print(form.recommendation_name.data)
        recommendation_name = form.recommendation_name.data
        recommendation_description = form.recommendation_description.data
        recommendation_location = form.recommendation_location.data
        recommendation_website = form.recommendation_website.date
        # recommendation_category = form.recommendation_category.data
        recommendation_author = form.recommendation_author.data
        recommendation_discount = form.recommendation_discount.data

        if len(recommendation_name) == 0 or len(recommendation_description) == 0 or len(recommendation_location) == 0 or len(recommendation_website) == 0:
            error = "Please supply both name, description, location and website details"
        else:
            recommendation = Recommendations(recommendation_name=recommendation_name, recommendation_description= recommendation_description,
                                             recommendation_location=recommendation_location, recommendation_website=recommendation_website,
                                             recommendation_author=recommendation_author, recommendation_discount=recommendation_discount)
                                            # add this when ready:  recommendation_category=recommendation_category

            service.add_new_recommendations(recommendation)
            recommendations = service.get_all_recommendations()

    return render_template("recommendations.html", form=form, message=error)




@routes.route('/discounts')
def discounts():
    # return "<h1>Discounts Page</h1>"
    return render_template("discounts.html")




