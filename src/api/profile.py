from flask import jsonify, Response

from src.services.tokens import token_required
from src.config.app import app


@app.route('/profile')
@token_required
def profile() -> Response:
    return jsonify({'info': 'If you see this, then you logged in'})
