from application import db
from dataclasses import dataclass


# the annotation below will help to turn the Python object into a JSON object
# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object

@dataclass
class Recommendations(db.Model):
    # the declarations below are important for turning the object into JSON
    recommendations_id: int
    recommendation_name: str
    recommendation_description: str
    recommendation_location: str
    recommendation_website: str
    # recommendation_category: str
    # google how to map an image for above
    recommendation_author: str
    recommendation_discount: int

    # add primary key below
    # we're storing all of our recommended restaurants in a schema looking like below:
    recommendations_id = db.Column(db.Integer, primary_key=True)
    recommendation_name = db.Column(db.String(100), nullable=False)
    recommendation_description = db.Column(db.String(1000), nullable=False)
    recommendation_location = db.Column(db.String(100), nullable=False)
    recommendation_website = db.Column(db.String(100), nullable=False)
    # recommendation_category = db.Column(db.String(100), nullable=False)
    recommendation_author = db.Column(db.String(100), nullable=True)
    recommendation_discount = db.Column(db.Integer, nullable=True)


# we don't have a foreign key for recommendations inputted right?


# database model = an object/ blueprint in which our database will be stored
# so above is telling system, all recommendations given need to look
# like the content held in the class called Recommendations above

