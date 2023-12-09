"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, jsonify, flash, request
from flask_debugtoolbar import DebugToolbarExtension


from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_pets():
    """List all the pets from the db to the Homepage"""

    pets = Pet.query.all()

    return render_template("/pets/pet_list.html", pets=pets)

@app.route("/add", methods=["GET","POST"])
def add_pet_form():
    """Add pet form with data handling"""

    form = AddPetForm()

    if form.validate_on_submit():
        from_form_name = form.name.data
        from_form_species = form.species.data
        from_form_photo_url = form.photo_url.data
        from_form_age = form.age.data
        from_form_notes = form.notes.data

        new_pet = Pet(name=from_form_name,
                species=from_form_species,
                photo_url=from_form_photo_url,
                age=from_form_age,
                notes=from_form_notes)

        db.session.add(new_pet)

        db.session.commit()

        flash(f"Pet {new_pet.name} available for adoption!")

        return redirect("/")

    else:
        return render_template("/pets/add_pet_form.html")


