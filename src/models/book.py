import uuid
import datetime

class Book:
    def __init__(self, isbn, title, author, genre, publication_year):
        self.book_id = str(uuid.uuid4())
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.section = None
        self.is_borrowed = False
        self.borrowed_by = None  # member_id
        self.borrow_date = None
        self.due_date = None
        self.borrowing_history = []  # list of dictionaries with borrowing records
        # Add more attributes as needed
    
    def borrow(self, member_id):
        """Mark book as borrowed and set due date (14 days from now)"""
        self.is_borrowed = True
        self.borrowed_by = member_id
        self.borrow_date = datetime.datetime.now()
        self.due_date = self.borrow_date + datetime.timedelta(days=14)
        
    def return_book(self):
        """Return the book and calculate if overdue"""
        return_date = datetime.datetime.now()
        overdue_days = 0
        late_fee = 0.0
        
        if return_date > self.due_date:
            overdue_days = (return_date - self.due_date).days
            late_fee = overdue_days * 0.50
        
        # Record in history
        self.borrowing_history.append({
            'member_id': self.borrowed_by,
            'borrow_date': self.borrow_date,
            'due_date': self.due_date,
            'return_date': return_date,
            'overdue_days': overdue_days,
            'late_fee': late_fee
        })
        
        # Reset borrowing status
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrow_date = None
        self.due_date = None
        
        return overdue_days, late_fee