from flask import request, jsonify, Response, session
from werkzeug.security import generate_password_hash, check_password_hash

from src.services.tokens import token_required, create_access_token, create_refresh_token, refresh_required
from src.models.user import User
from src.config.app import db, app


@app.route('/login', methods=['POST'])
def login() -> Response:
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()
    if request_data['email'] and check_password_hash(user.password, str(request_data['password'])):
        session['logged_in'] = True

        access_token = create_access_token(request_data)
        refresh_token = create_refresh_token(request_data)

        return jsonify({'access_token': access_token.decode('UTF-8'),
                        'refresh_token': refresh_token.decode('UTF-8')})

    return jsonify({'info': 'something wrong'})


@app.route('/refresh')
@refresh_required
def refresh_token() -> Response:

    request_data = request.get_json()
    access_token = create_access_token(request_data)
    refresh_token = create_refresh_token(request_data)

    return jsonify({'access_token': access_token.decode('UTF-8'),
                    'refresh_token': refresh_token.decode('UTF-8')})


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


@app.route('/profile')
@token_required
def profile() -> Response:
    return jsonify({'info': 'If you see this, then you logged in'})
