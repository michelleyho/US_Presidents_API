# app.py

from flask import render_template # Remove: import Flask
#import connexion
import config
from models import President

#application = connexion.FlaskApp(__name__)
#application.add_api("swagger.yml")

#app = application.app

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
