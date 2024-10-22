from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import routes # noqa

app.register_blueprint(routes.api, url_prefix='/api/v1')
app.register_blueprint(routes.client, url_prefix='/client')
