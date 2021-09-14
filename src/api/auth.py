from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.user import User
from src.config.app import db, app


@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    email = request_data['email']
    password = str(request_data['password'])
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'info': 'smth wrong'})

    return jsonify({'info': 'you are log IN'})


@app.route('/signup', methods=['POST'])
def signup():
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


@app.route('/logout')
def logout():
    return jsonify({'info': 'you are log OUT'})


@app.route('/profile')
def profile():
    return 'str'


@app.route('/')
def index():
    return jsonify({'page': 'main page'})


