from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config.env_consts import ENV_CONSTS

db = SQLAlchemy()

app = Flask(__name__)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = ENV_CONSTS['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = ENV_CONSTS['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

from src.api.auth import app