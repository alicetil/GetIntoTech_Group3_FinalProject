from flask import Blueprint, render_template, jsonify


auth = Blueprint('auth', __name__)

# JUST-IN-CASE-AUTHENTICATION-ROUTE-FILE
# WE MIGHT NEED THIS PAGE FOR USER AUTHENTICATION STUFF e.g. login/subscribe etc


# Not added to Nav Bar (as a bit crowded atm)
@auth.route('/contact')
def contact():
    # return "<h1>Contact Us Page</h1>"
    return render_template("contact.html")

