from application import db
from dataclasses import dataclass

@dataclass
class local_events(db.Model):
    id : int
    event_name: str
    event_location: str
    event_start_date: datetime
    event_end_date: datetime
    event_website: str
    #event_image : imghdr
    event_category: str

    id = db.Column(db.Integer, primary_key=True)
    event_name= db.Column(db.String(100),nullable=False)
    event_location = db.Column(db.String(1000),nullable=False)
    event_start_date = db.Column(db.DateTime(100),nullable=True)
    event_end_date = db.Column(db.DateTime(100),nullable=True)
    #outdoor_image
    event_website =db.Column(db.String(100),nullable=False)
    # event_image : imghdr
    event_category = db.Column(db.String(100),nullable=True)