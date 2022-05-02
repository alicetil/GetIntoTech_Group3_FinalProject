from website import db
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
    recommendation_author: str
    recommendation_discount: int

    recommendation_name = db.Column(db.String(100), nullable=False)
    recommendation_description = db.Column(db.String(1000), nullable=False)
    recommendation_location = db.Column(db.String(100), nullable=False)
    recommendation_website = db.Column(db.String(100), nullable=False)
    # recommendation_category = db.Column(db.String(100), nullable=False)
    recommendation_author = db.Column(db.String(100), nullable=True)
    recommendation_discount = db.Column(db.Integer, nullable=True)
