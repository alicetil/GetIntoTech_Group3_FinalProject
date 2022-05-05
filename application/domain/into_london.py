from application import db
from dataclasses import dataclass

@dataclass
class into_london(db.Model):
    id : int
    london_name: str
    london_location: str
    london_travel: str
    london_website: str
    #london_image : imghdr
    london_description: str
    london_category: str
    london_affordabiltiy: str
    london_discount: str

    id = db.Column(db.Integer, primary_key=True)
    london_name= db.Column(db.String(100),nullable=False)
    london_location = db.Column(db.String(1000),nullable=False)
    london_travel = db.Column(db.String(100), nullable=False)
    london_website = db.Column(db.String(100), nullable=False)
    #london_image
    london_description = db.Column(db.String(1000),nullable=False)
    london_category = db.Column(db.String(1000),nullable=True)
    london_affordabiltiy = db.Column(db.String(100),nullable=True)
    london_discount = db.Column(db.String(1000),nullable=False)