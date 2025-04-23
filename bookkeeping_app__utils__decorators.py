from functools import wraps
from flask import request, jsonify
from app.utils.firebase import verify_firebase_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        decoded_token = verify_firebase_token(token)

        if not decoded_token:
            return jsonify({'message': 'Invalid token!'}), 401

        # Pass user info to route
        return f(decoded_token, *args, **kwargs)

    return decorated
