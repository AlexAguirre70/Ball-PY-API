from flask import(Blueprint, render_template,request,redirect)
from . import models

bp=Blueprint('reptile',__name__,url_prefix='/reptiles')

# Get all of Reptiles in Json
@bp.route('/', methods=['GET','POST'])
def Index():
    if request.method == "POST":
        newName= request.form['name']
        newType= request.form['reptile_type']
        newInfo= request.form['info']

        newReptile=models.Reptile(name=newName,reptile_type=newType,info=newInfo)
        models.db.session.add(newReptile)
        models.db.session.commit()

        return redirect('../')

    return "This returns the list of reptiles"
# Get a reptile by ID route
@bp.route('/<int:id>')
def getReptile(id):
    return "This returns a reptile by ID"


# Get Add Reptile form route
@bp.route('/new')
def new_reptile():
    return render_template('new.html')


