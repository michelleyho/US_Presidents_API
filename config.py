# config.py

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()

#application = connexion.FlaskApp(__name__)
#application.add_api("swagger.yml")

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app
#app = application.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'presidents.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


