from flask import Blueprint, jsonify
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({'page': 'main page'})


@login_required
@main.route('/profile')
def profile():
    return jsonify({'page': f'{current_user.name} profile'})
