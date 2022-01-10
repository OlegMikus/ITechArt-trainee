from flask import jsonify, Response

from src.services.tokens import token_required
from src.config.app import app


@app.route('/logout')
@token_required
def logout() -> Response:
    access_token = None
    ref_token = None
    return jsonify({'access_token': access_token,
                    'refresh_token': ref_token,
                    'info': 'If you see this, then you logged OUT'})
