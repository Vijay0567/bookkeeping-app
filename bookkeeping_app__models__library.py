from app import db

class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150))

    books = db.relationship('Book', backref='library', lazy=True)
