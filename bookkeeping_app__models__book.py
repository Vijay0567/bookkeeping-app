from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    cover_image = db.Column(db.String(255))  # Firebase URL
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'cover_image': self.cover_image,
            'author_id': self.author_id,
            'borrower_id': self.borrower_id,
            'library_id': self.library_id
        }
