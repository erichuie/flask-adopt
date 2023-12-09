"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    name = StringField("Give it a name: ",
                       validators=[InputRequired()])
    species = StringField("What animal: ",
                          validators=[InputRequired()])
    photo_url = StringField("Give an image url: ",
                            validators=[Optional(),URL()])
    age = SelectField("Pick from the list of ages: ",
                    choices= [("baby","baby"),
                              ("young","young"),
                              ("adult","adult"),
                              ("senior","senior")],
                    validators=[InputRequired()])
    notes = TextAreaField("Tell us notes about your animal: ",
                          validators=[Optional()])