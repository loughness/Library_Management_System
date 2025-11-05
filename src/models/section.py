import uuid
import datetime

class Section:
    def __init__(self, name, floor, capacity):
        self.section_id = str(uuid.uuid4())
        self.name = name
        self.floor = floor
        self.capacity = capacity
        self.books = []  # list of book_ids
        self.last_cleaned = None
        self.librarian_id = None  # librarian responsible for this section
        # Add more attributes as needed
    
    def add_book(self, book_id):
        """Add a book to this section"""
        if len(self.books) < self.capacity:
            self.books.append(book_id)
            return True
        return False
    
    def remove_book(self, book_id):
        """Remove a book from this section"""
        if book_id in self.books:
            self.books.remove(book_id)
            return True
        return False
    
    def clean(self):
        """Mark section as cleaned"""
        self.last_cleaned = datetime.datetime.now()
    
    def is_at_capacity(self):
        """Check if section is at maximum capacity"""
        return len(self.books) >= self.capacity

