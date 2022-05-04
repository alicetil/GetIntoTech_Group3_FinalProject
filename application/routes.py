from flask import Blueprint, render_template, jsonify, request

from application import service, app
from application.domain.recommendations import Recommendations
from application.forms.recommendationsForm import RecommendForm

# routes = Blueprint('routes', __name__)


@app.route('/')
def home():
    # return "<h1>Testing this home page route</h1>"
    return render_template("home.html")


@app.route('/placestoeat')
def places_to_eat():
    # return "<h1>Places to eat page </h1>"
    return render_template("placestoeat.html")


@app.route('/exploretheoutdoors')
def explore_the_outdoors():
    # return "<h1>Explore the outdoors page</h1>"
    return render_template("exploretheoutdoors.html")


@app.route('/intothecitycentre')
def into_city_centre():
    # return "<h1>Explore the city centre page</h1>"
    return render_template("intothecitycentre.html")


@app.route('/localevents')
def local_events():
    # return "<h1>Explore the local events page</h1>"
    return render_template("localevents.html")


@app.route('/recommendations', methods=['GET','POST'])
def add_recommendations():
    error = ""
    form = RecommendForm()

    if request.method == "POST":
        form = RecommendForm(request.form)
        print(form.recommendation_name.data)
        recommendation_name = form.recommendation_name.data
        recommendation_description = form.recommendation_description.data
        recommendation_location = form.recommendation_location.data
        recommendation_website = form.recommendation_website.data
        recommendation_category = form.recommendation_category.data
        recommendation_author = form.recommendation_author.data
        recommendation_discount = form.recommendation_discount.data

        if len(recommendation_name) == 0 or len(recommendation_description) == 0 or len(recommendation_location) == 0 or len(recommendation_website) == 0:
            error = "you're missing one of these: name, description, location and website details. Please supply."
        else:
            recommendation = Recommendations(recommendation_name=recommendation_name, recommendation_description= recommendation_description,
                                             recommendation_location=recommendation_location, recommendation_website=recommendation_website,
                                             recommendation_category=recommendation_category, recommendation_author=recommendation_author,
                                             recommendation_discount=recommendation_discount)

            service.add_new_recommendations(recommendation)
            recommendations = service.get_all_recommendations()
            return render_template('list_recommendations.html', recommendations=recommendations, message=error)

    return render_template('recommendations.html', form=form, message=error)


@app.route('/list', methods=['GET'])
def show_recomm_list():
    # return "<h1>Recommendations List Page</h1>"
    error = ""
    recommendations = service.get_all_recommendations()
    if len(recommendations) == 0:
        error = "There are no recommendations to display. Do add one!"
    return render_template("list_recommendations.html", recommendations=recommendations, message=error)



@app.route('/discounts')
def discounts():
    # return "<h1>Discounts Page</h1>"
    return render_template("discounts.html")




