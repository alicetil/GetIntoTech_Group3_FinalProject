from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField


class RecommendForm(FlaskForm):
    recommendation_name = StringField("Restaurant Name")
    recommendation_description = StringField("Brief Description")
    recommendation_location = StringField("Location")
    recommendation_website = StringField("Website Link")
    # option below for category
    recommendation_category = StringField("")
    recommendation_author = StringField("Author's Name")
    recommendation_discount = IntegerField("Discount Amount")

    submit = SubmitField("Add Recommended Restaurant")
