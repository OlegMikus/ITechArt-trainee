import jwt
from flask import request, jsonify, Response

from src.services.tokens import create_tokens
from src.config.app import app


@app.route('/refresh')
def refresh_token() -> Response:
    token = request.headers['refresh_token']

    if not refresh_token:
        return jsonify({'Alert!': ' refresh Token is missing!'})
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])

        request_data = request.get_json()
        tokens = create_tokens(request_data)
        access_token = tokens['access_token']
        ref_token = tokens['refresh_token']

        return jsonify({'access_token': access_token.decode('UTF-8'),
                        'refresh_token': ref_token.decode('UTF-8'),
                        'redirect-url': 'http://localhost:8000/profile'})

    except jwt.InvalidTokenError:
        return jsonify({'Message': 'Invalid refresh token. Please log in again.'})
