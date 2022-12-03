## Creating an API with Flask<br><br>
Overall, the process for creating an API with Flask is the same as we just learned:<br><br>

* Create a virtual environment.<br>
* Install and import Flask.<br>
* Create an application factory.<br>
* Import and invoke the application factory on a root app.py file.<br>
* Create the database in Postgres and configure it within the app using Flask-SQLAlchemy.<br>
* Create the database instance and all necessary models.<br>
* Create blueprints and all necessary routes.<br>
* Import the database models into the application factory.<br>
* Import and register all blueprints onto the application factory.<br>
* Import and install Flask-Migrate to migrate the database changes.<br>
* Don't forget to run the migration commands in your virtual environment whenever you create a new model.<br>
* Also, don't forget to install the psycopg2 package to allow Python to work with Postgres.<br>