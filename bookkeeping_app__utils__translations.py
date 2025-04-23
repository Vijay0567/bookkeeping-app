from flask_babel import gettext

def get_translated_message(key):
    messages = {
        "missing_fields": gettext("Missing required fields!"),
        "registration_success": gettext("Registration successful."),
        "registration_failed": gettext("Registration failed."),
        "login_success": gettext("Login successful."),
        "invalid_credentials": gettext("Invalid credentials."),
        "unauthorized_role": gettext("Unauthorized role for this action."),
        "book_added": gettext("Book successfully added."),
        "book_deleted": gettext("Book successfully deleted."),
        "unauthorized_delete": gettext("You are not authorized to delete this book."),
        "book_not_found": gettext("Book not found."),
        "book_already_borrowed": gettext("This book is already borrowed."),
        "book_borrowed": gettext("Book successfully borrowed."),
        "book_returned": gettext("Book successfully returned."),
        "library_added": gettext("Library successfully added."),
    }
    return messages.get(key, key)
