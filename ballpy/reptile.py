from flask import(Blueprint, render_template,request)

bp=Blueprint('reptile',__name__,url_prefix='/reptiles')

# Get all of Reptiles in Json

# Get a reptile by ID route

# Get Add Reptile form route
@bp.route('/new')
def new_reptile():
    return render_template('reptiles/new.html')


# Add Reptile to database route



