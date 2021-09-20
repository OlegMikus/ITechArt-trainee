from datetime import datetime, timedelta
from functools import wraps
from typing import Any

import jwt
from flask import request, jsonify, Response

from src.config.app import app


def token_required(func: Any) -> Any:
    @wraps(func)
    def decorated(*args: Any, **kwargs: Any) -> Response:
        token = request.headers['token']
        if not token:
            return jsonify({'Alert!': 'Token is missing!'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print(data)
        except jwt.ExpiredSignatureError:
            return jsonify({'Message': 'http://localhost:8000/refresh'})
        except jwt.InvalidTokenError:
            return jsonify({'Message': 'Invalid token. Please log in again.'})
        return func(*args, **kwargs)

    return decorated


def refresh_required(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Response:
        token = request.headers['refresh_token']
        if not token:
            return jsonify({'Alert!': ' refresh Token is missing!'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print(data)
        except jwt.InvalidTokenError:
            return jsonify({'Message': 'Invalid refresh token. Please log in again.'})
        return func(*args, **kwargs)

    return wrapper


def create_access_token(data: Any) -> bytes:
    token = jwt.encode({
        'user_email': data['email'],
        'exp': datetime.utcnow() + timedelta(seconds=60),
    },
        app.config['SECRET_KEY'])
    return token


def create_refresh_token(data: Any) -> bytes:
    token = jwt.encode({
        'user_email': data['email'],
        'exp': datetime.utcnow() + timedelta(days=30),
    },
        app.config['SECRET_KEY'])
    return token
