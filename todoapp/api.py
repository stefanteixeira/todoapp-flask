import flask.ext.restless
from todoapp.apps import db
from todoapp.models import Todo
import os

app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Todo, methods=['GET', 'POST','PUT', '\DELETE'])



if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=5001)
