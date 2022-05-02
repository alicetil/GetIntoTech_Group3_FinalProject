# import SQLAlchemy as SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import main_app


# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/visiting_sky_db"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
#
#     # what does the below mean?
#     # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@host/database_name"
#     # app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
#
#     from .routes import routes
#     from .auth import auth
#
#     app.register_blueprint(routes, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')
#
#     # db = SQLAlchemy(app)
#
#     return app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/visiting_sky_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# what does the below mean?
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@host/database_name"
# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))

# make things run 1st before u add the below:
# from .routes import routes
# from .auth import auth

# app.register_blueprint(routes, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')

db = SQLAlchemy(app)


# app = create_app()
# db = SQLAlchemy(app)







# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/visiting_sky_db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'anything'
#
#
#
# # link our app to the persistence layer
# db = SQLAlchemy(app)


# # app = create_app()
# # db = SQLAlchemy(create_app())
# db = SQLAlchemy(app)


