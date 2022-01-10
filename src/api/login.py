from flask import request, jsonify, Response
from werkzeug.security import check_password_hash

from src.services.tokens import create_tokens
from src.models.user import User
from src.config.app import app


@app.route('/login', methods=['POST'])
def login() -> Response:
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()
    if request_data['email'] and check_password_hash(user.password, str(request_data['password'])):

        tokens = create_tokens(request_data)
        access_token = tokens['access_token']
        ref_token = tokens['refresh_token']

        return jsonify({'access_token': access_token.decode('UTF-8'),
                        'refresh_token': ref_token.decode('UTF-8')})

    return jsonify({'info': 'something wrong'})
