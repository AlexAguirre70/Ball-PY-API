from flask import(Blueprint, render_template,request)
from . import models

bp=Blueprint('reptile',__name__,url_prefix='/reptiles')

# Get all of Reptiles in Json

# Get a reptile by ID route

# Get Add Reptile form route
@bp.route('/new')
def new_reptile():
    return render_template('new.html')

# Add Reptile to database route
@bp.route('/',methods=["POST"])
def Index_Add():
    if request.method == "POST":
        newName= request.form['name']
        newType= request.form['reptile_type']
        newInfo= request.form['info']

        newReptile=models.Reptile(name=newName,reptile_type=newType,info=newInfo)
        models.db.session.add(newReptile)
        models.db.session.commit()

        return render_template('index.html')


