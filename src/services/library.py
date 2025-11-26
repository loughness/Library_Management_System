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
        # TODO: apply list comprehension
        for book in self.books:
            if not book.is_borrowed:
                available_books.append(book)
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
    
    def redistribute_section(self, librarian_id):
        leaving_librarian = self.get_librarian(librarian_id)
        
        if leaving_librarian is None:
            return False, "librarian_not_found"
        else:
            total_librarians = len(self.librarians)

            if total_librarians - 1 <= 0:
                return False, "no_other_librarians"
            else:
                # remove leaving librarian
                self.remove_librarian(leaving_librarian)

                # while the leaving librarian still has sections...
                while leaving_librarian.sections:
                    least_num_sections = len(self.librarians[0].sections)
                    least_num_section_librarian = self.librarians[0]

                    for librarian in self.librarians:
                        # getting the librarians number of sections
                        num_lib_sections = len(librarian.sections)
                        # if the librarians number of sections is less than the least number of sections
                        # assign this as the least number of sections
                        # save which librarian this is
                        if num_lib_sections < least_num_sections:
                            least_num_sections = num_lib_sections
                            least_num_section_librarian = librarian
                    
                    # append the leaving librarian first section to another librarian
                    section = leaving_librarian.sections[0]
                    # remove this section from old librarian
                    leaving_librarian.remove_section(section)
                    # add section to 'new' librarian
                    least_num_section_librarian.assign_section(section)

                return True, "ok"