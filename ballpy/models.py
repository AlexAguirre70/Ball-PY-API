from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#define the class
class Reptile(db.Model):
    __tablename__="reptiles"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    reptile_type=db.Column(db.String)
    info=db.Column(db.Text)
