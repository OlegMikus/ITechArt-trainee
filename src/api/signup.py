from flask import request, jsonify, Response
from werkzeug.security import generate_password_hash

from src.models.user import User
from src.config.app import db, app


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
