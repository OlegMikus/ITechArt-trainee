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


def create_tokens(data: Any) -> dict:
    access_token = jwt.encode({
        'user_email': data['email'],
        'exp': datetime.utcnow() + timedelta(seconds=180),
    },
        app.config['SECRET_KEY'])
    refresh_token = jwt.encode({
        'user_email': data['email'],
        'exp': datetime.utcnow() + timedelta(days=30),
    },
        app.config['SECRET_KEY'])

    tokens = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return tokens
