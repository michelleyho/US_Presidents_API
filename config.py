# config.py

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
data_dir = basedir / "data"
data_dir.mkdir(exist_ok=True)

if not data_dir.exists():
    data_dir = basedir

#application = connexion.FlaskApp(__name__)
#application.add_api("swagger.yml")

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app
#app = application.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{data_dir /'presidents.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


