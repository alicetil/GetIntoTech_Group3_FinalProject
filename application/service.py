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

