import os

from flask import Flask
from database import database
from api import routes

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getcwd()}/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

database.init_app(app)
app.register_blueprint(routes.api)

if __name__ == "__main__":
	app.run(debug=True)
