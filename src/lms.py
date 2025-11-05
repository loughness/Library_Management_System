from flask import Flask, jsonify
from flask_restx import Api, reqparse, Resource
from utils.library_json_utils import LibraryJsonEncoder
from services.library import Library
from models.book import Book
from models.member import Member
from models.section import Section
from models.librarian import Librarian

# Initialize library
my_library = Library()

# Initialize Flask app
lms_app = Flask(__name__)
lms_app.json_encoder = LibraryJsonEncoder
lms_api = Api(lms_app)

# Request parsers
book_parser = reqparse.RequestParser()
book_parser.add_argument('isbn', type=str, required=True, help='ISBN of the book')
book_parser.add_argument('title', type=str, required=True, help='Title of the book')
book_parser.add_argument('author', type=str, required=True, help='Author of the book')
book_parser.add_argument('genre', type=str, required=True, help='Genre of the book')
book_parser.add_argument('publication_year', type=int, required=True, help='Publication year')

member_parser = reqparse.RequestParser()
member_parser.add_argument('name', type=str, required=True, help='Name of the member')
member_parser.add_argument('email', type=str, required=True, help='Email of the member')
member_parser.add_argument('phone', type=str, required=True, help='Phone number')

section_parser = reqparse.RequestParser()
section_parser.add_argument('name', type=str, required=True, help='Name of the section')
section_parser.add_argument('floor', type=int, required=True, help='Floor number')
section_parser.add_argument('capacity', type=int, required=True, help='Maximum capacity')

# ============================================
# BOOK ENDPOINTS (Examples provided)
# ============================================

@lms_api.route('/book')
class AddBookAPI(Resource):
    @lms_api.doc(parser=book_parser)
    def post(self):
        """Add a new book to the library"""
        args = book_parser.parse_args()
        new_book = Book(
            args['isbn'],
            args['title'],
            args['author'],
            args['genre'],
            args['publication_year']
        )
        my_library.add_book(new_book)
        return jsonify(new_book)


@lms_api.route('/book/<book_id>')
class BookAPI(Resource):
    def get(self, book_id):
        """Get details of a specific book"""
        book = my_library.get_book(book_id)
        if not book:
            return jsonify({"error": f"Book with ID {book_id} not found"}), 404
        return jsonify(book)
    
    def delete(self, book_id):
        """Delete a book (only if not borrowed)"""
        book = my_library.get_book(book_id)
        if not book:
            return jsonify({"error": f"Book with ID {book_id} not found"}), 404
        if book.is_borrowed:
            return jsonify({"error": "Cannot delete a borrowed book"}), 400
        my_library.remove_book(book)
        return jsonify({"message": f"Book {book_id} deleted successfully"})


@lms_api.route('/books')
class AllBooksAPI(Resource):
    def get(self):
        """Get all books in the library"""
        return jsonify(my_library.books)


@lms_api.route('/book/<book_id>/borrow')
class BorrowBookAPI(Resource):
    def post(self, book_id):
        """Borrow a book"""
        # You need to implement this - parse member_id from request
        # Check if book is available
        # Check if member can borrow more books
        # Update book and member objects
        pass


@lms_api.route('/book/<book_id>/return')
class ReturnBookAPI(Resource):
    def post(self, book_id):
        """Return a book"""
        # You need to implement this
        # Calculate overdue fees
        # Update book and member objects
        pass


# ============================================
# MEMBER ENDPOINTS (You need to implement these)
# ============================================

@lms_api.route('/member')
class AddMemberAPI(Resource):
    @lms_api.doc(parser=member_parser)
    def post(self):
        """Add a new member"""
        args = member_parser.parse_args()
        new_member = Member(args['name'], args['email'], args['phone'])
        my_library.add_member(new_member)
        return jsonify(new_member)


@lms_api.route('/members')
class AllMembersAPI(Resource):
    def get(self):
        """Get all members"""
        return jsonify(my_library.members)


# Add more member endpoints here...


# ============================================
# SECTION ENDPOINTS (You need to implement these)
# ============================================

@lms_api.route('/section')
class AddSectionAPI(Resource):
    @lms_api.doc(parser=section_parser)
    def post(self):
        """Add a new section"""
        args = section_parser.parse_args()
        new_section = Section(args['name'], args['floor'], args['capacity'])
        my_library.add_section(new_section)
        return jsonify(new_section)


# Add more section endpoints here...


# ============================================
# LIBRARIAN ENDPOINTS (You need to implement these)
# ============================================

# Add librarian endpoints here...


# ============================================
# TASK ENDPOINTS (You need to implement these)
# ============================================

# Add task generation endpoints here...


if __name__ == '__main__':
    lms_app.run(debug=False, port=7891)