from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config.env_consts import ENV_CONSTS

db: SQLAlchemy = SQLAlchemy()

app: Flask = Flask(__name__)
migrate = Migrate(app, db, directory='src/models/migrations')
app.config['SECRET_KEY'] = ENV_CONSTS['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = ENV_CONSTS['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from src.api import app
