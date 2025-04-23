from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.book import Book
from app.models.user import User
from app import db
from flask_babel import _

borrow_bp = Blueprint('borrow', __name__)

@borrow_bp.route('/borrow/<int:book_id>', methods=['POST'])
@jwt_required()
def borrow_book(book_id):
    current_user = User.query.get(get_jwt_identity())
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'message': _('Book not found.')}), 404

    if book.borrowed_by:
        return jsonify({'message': _('Book is already borrowed.')}), 400

    book.borrowed_by = current_user.id
    db.session.commit()

    return jsonify({'message': _('Book borrowed successfully.'), 'book': book.to_dict()}), 200


@borrow_bp.route('/return/<int:book_id>', methods=['POST'])
@jwt_required()
def return_book(book_id):
    current_user = User.query.get(get_jwt_identity())
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'message': _('Book not found.')}), 404

    if book.borrowed_by != current_user.id:
        return jsonify({'message': _('You cannot return a book you did not borrow.')}), 403

    book.borrowed_by = None
    db.session.commit()

    return jsonify({'message': _('Book returned successfully.'), 'book': book.to_dict()}), 200
