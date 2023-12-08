from app import app
from models import db, Pet

db.drop_all()
db.create_all()

pet = Pet(name="Fluffy", species="cat", age="adult", available=True)

db.session.add(pet)
db.session.commit()