from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from flaskapp.models import User
from flaskapp import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_post():
    request_data = request.get_json()
    email = request_data['email']
    password = str(request_data['password'])
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'info': 'smth wrong'})

    login_user(user)

    return jsonify({'info': 'you are log IN'})


@auth.route('/signup', methods=['POST'])
def signup_post():
    request_data = request.get_json()
    email = request_data['email']
    name = request_data['name']
    password = str(request_data['password'])

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'info': 'smth wrong'})

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'info': 'congratulation'})


@auth.route('/logout')
def logout():
    logout_user()
    return jsonify({'info': 'you are log OUT'})
