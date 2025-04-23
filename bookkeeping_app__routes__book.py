from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.book import Book
from app.models.user import User
from app.models.library import Library
from app import db
from flask_babel import _

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    current_user = User.query.get(get_jwt_identity())

    if current_user.role != 'author':
        return jsonify({'message': _('Only authors can add books.')}), 403

    data = request.get_json()
    if not all(key in data for key in ['title', 'library_id', 'cover_image']):
        return jsonify({'message': _('Missing book fields.')}), 400

    library = Library.query.get(data['library_id'])
    if not library:
        return jsonify({'message': _('Library not found.')}), 404

    book = Book(
        title=data['title'],
        author_id=current_user.id,
        library_id=data['library_id'],
        cover_image=data['cover_image']
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({'message': _('Book added successfully.'), 'book': book.to_dict()}), 201


@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    current_user = User.query.get(get_jwt_identity())
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'message': _('Book not found.')}), 404

    if current_user.role != 'author' or book.author_id != current_user.id:
        return jsonify({'message': _('Not authorized to delete this book.')}), 403

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': _('Book deleted successfully.')}), 200


@book_bp.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200
