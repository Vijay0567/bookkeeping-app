from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.library import Library
from app import db
from flask_babel import _

library_bp = Blueprint('library', __name__)

@library_bp.route('/libraries', methods=['POST'])
@jwt_required()
def add_library():
    data = request.get_json()
    if not all(key in data for key in ['name', 'location']):
        return jsonify({'message': _('Missing required fields.')}), 400

    library = Library(
        name=data['name'],
        location=data['location']
    )

    db.session.add(library)
    db.session.commit()

    return jsonify({'message': _('Library added successfully.'), 'library': library.to_dict()}), 201


@library_bp.route('/libraries/<int:library_id>', methods=['PUT'])
@jwt_required()
def update_library(library_id):
    library = Library.query.get(library_id)
    if not library:
        return jsonify({'message': _('Library not found.')}), 404

    data = request.get_json()
    library.name = data.get('name', library.name)
    library.location = data.get('location', library.location)

    db.session.commit()

    return jsonify({'message': _('Library updated successfully.'), 'library': library.to_dict()}), 200


@library_bp.route('/libraries', methods=['GET'])
@jwt_required()
def get_libraries():
    libraries = Library.query.all()
    return jsonify([library.to_dict() for library in libraries]), 200
