from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)


# add SQLAlchemy config
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ballpy_user:ballpy$123@localhost:5432/ballpy'
    app.config ['SQLALCHEMY_TRACK_MODIFICATION'] = False

# import the database model
    from . import models
    models.db.init_app(app)

# Instantiate Migrate
    migrate = Migrate(app, models.db)

#register the blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)

    return app