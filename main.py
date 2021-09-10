from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
def index():  # put application's code here
    return render_template('index.html')


@login_required
@main.route('/profile')
def profile():
    return jsonify(current_user)
