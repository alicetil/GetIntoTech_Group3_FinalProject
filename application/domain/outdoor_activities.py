from application import db
from dataclasses import dataclass

@dataclass
class OutdoorActivities(db.Model):
    id : int
    outdoor_name: str
    outdoor_address: str
    outdoor_website: str
    #outdoor_image : imghdr
    outdoor_descriptions: str
    outdoor_affordability: str
    outdoor_discount: str

    id = db.Column(db.Integer, primary_key = True)
    outdoor_name = db.Column(db.String(100),nullable =False)
    outdoor_address = db.Column(db.String(1000),nullable =False)
    outdoor_website = db.Column(db.String(100),nullable =False)
    #outdoor_image
    outdoor_descriptions =db.Column(db.String(1000),nullable =True)
    outdoor_affordability = db.Column(db.String(1000),nullable =True)
    outdoor_discount = db.Column(db.String(100),nullable =True)
