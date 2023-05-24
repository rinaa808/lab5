from flask import Flask
from flask_migrate import Migrate
from db import db
from config import Config
from models import Employee, Position, Division, Job # noqa

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    ...


if __name__ == '__main__':
    app.run()
