from datetime import datetime, timedelta
from functools import wraps
from typing import Any

import jwt
from flask import request, jsonify, Response, session
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.user import User
from src.config.app import db, app


def token_required(func: Any) -> Any:
    @wraps(func)
    def decorated(*args: Any, **kwargs: Any) -> Response:
        token = request.headers['token']
        if not token:
            return jsonify({'Alert!': 'Token is missing!'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.InvalidTokenError:
            return jsonify({'Message': 'Invalid token. Please log in again.'})
        return func(data, *args, **kwargs)

    return decorated


@app.route('/login', methods=['POST'])
def login() -> Response:
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()
    if request_data['email'] and check_password_hash(user.password, str(request_data['password'])):
        token = jwt.encode({'user_email': request_data['email'],
                            'expiration': str(datetime.utcnow() + timedelta(seconds=60))},
                           app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return jsonify({'info': 'something wrong'})


@app.route('/signup', methods=['POST'])
def signup() -> Response:
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
@token_required
def logout() -> Response:
    ''' This function doesn't work '''
    if session['logged_in']:
        session['logged_in'] = False
        return jsonify({'message': 'You successfully logged out'})
    return jsonify({'message': 'error'})


@app.route('/profile')
@token_required
def profile() -> Response:
    request_data = request.get_json()
    return jsonify({'info': request_data, })
