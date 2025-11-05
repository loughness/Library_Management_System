import uuid
import datetime

class Member:
    MAX_BOOKS = 5  # Maximum books a member can borrow at once
    
    def __init__(self, name, email, phone):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_date = datetime.datetime.now()
        self.borrowed_books = []  # list of book_ids
        # Add more attributes as needed
    
    def can_borrow(self):
        """Check if member can borrow more books"""
        return len(self.borrowed_books) < self.MAX_BOOKS
    
    def borrow_book(self, book_id):
        """Add book to member's borrowed list"""
        if self.can_borrow():
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id):
        """Remove book from member's borrowed list"""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False