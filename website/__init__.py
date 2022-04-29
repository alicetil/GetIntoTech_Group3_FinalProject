import SQLAlchemy as SQLAlchemy
from flask import Flask

import main_app


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'anything'
#
#     from .routes import routes
#     from .auth import auth
#
#     app.register_blueprint(routes, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')
#
#     return app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/visiting_sky_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'anything'



# link our app to the persistence layer
db = SQLAlchemy(app)

