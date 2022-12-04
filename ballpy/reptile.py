from flask import(Blueprint, render_template,request,redirect)
from . import models
import json
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
        
    if request.method=="GET":
        results= models.Reptile.query.all()
        reptile_dict= []
        
        for reptile in results:
            addList={"id:"+str(reptile.id),"name:"+reptile.name,"reptile_type:"+reptile.reptile_type,"info:"+reptile.info}
            reptile_dict.append(addList)
        
        return json.dumps(reptile_dict)
    return "The list has been sent"

# Get a reptile by ID route
@bp.route('/<int:id>')
def getReptile(id):
    reptile = models.Reptile.query.filter_by(id=id).first()

    # Reptile information:  directory
    reptile_dict = {
        'id': reptile.id,
        'name': reptile.name,
        'reptile_type': reptile.reptile_type,
        'info': reptile.info
    }
    
    # return the dictionary, which will get returned as JSON by default
    return reptile_dict


# Get Add Reptile form route
@bp.route('/new')
def new_reptile():
    return render_template('new.html')


