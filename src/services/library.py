class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.sections = []
        self.librarians = []
    
    # Book methods
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    
    def available_books(self):
        available_books = []
        
        for book in self.books:
            if not book.is_borrowed:
                available_books.append(book)
        
        if len(available_books) <= 0:
            return {"message": "There are no available books..."}
        else:
            return available_books
    
    # Member methods
    def add_member(self, member):
        self.members.append(member)
    
    def remove_member(self, member):
        self.members.remove(member)
    
    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    # Section methods
    def add_section(self, section):
        self.sections.append(section)
    
    def remove_section(self, section):
        self.sections.remove(section)
    
    def get_section(self, section_id):
        for section in self.sections:
            if section.section_id == section_id:
                return section
        return None
    
    # Librarian methods
    def add_librarian(self, librarian):
        self.librarians.append(librarian)
    
    def remove_librarian(self, librarian):
        self.librarians.remove(librarian)
    
    def get_librarian(self, librarian_id):
        for librarian in self.librarians:
            if librarian.employee_id == librarian_id:
                return librarian
        return None