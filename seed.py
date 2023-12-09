from app import app
from models import db, Pet

db.drop_all()
db.create_all()

cat = Pet(name="Fluffy",
          species="cat",
          photo_url="https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=0.670xw:1.00xh;0.167xw,0&resize=640:*",
          age="adult",
          available=True)

dog = Pet(name="Snuffy",
          species="dog",
          photo_url="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*",
          age="baby",
          available=False)

db.session.add(cat)
db.session.add(dog)
db.session.commit()