import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.book import Book
from src.models.member import Member
from src.models.section import Section
from src.models.librarian import Librarian
from src.services.library import Library

@pytest.fixture
def library():
    return Library()


@pytest.fixture
def sample_book():
    return Book("978-0-123456-78-9", "Python Programming", "John Doe", "Technology", 2020)


@pytest.fixture
def sample_member():
    return Member("Alice Smith", "alice@example.com", "555-1234")


@pytest.fixture
def sample_section():
    return Section("Technology", 1, 100)

@pytest.fixture
def sample_librarian():
    return Librarian("Liam", "liam@loughystudios.com")


def test_add_book(library, sample_book):
    library.add_book(sample_book)
    assert sample_book in library.books
    assert len(library.books) == 1


def test_add_member(library, sample_member):
    library.add_member(sample_member)
    assert sample_member in library.members
    assert len(library.members) == 1


def test_borrow_book(sample_book, sample_member):
    # Book should not be borrowed initially
    assert sample_book.is_borrowed == False
    
    # Borrow the book
    sample_book.borrow(sample_member.member_id)
    sample_member.borrow_book(sample_book.book_id)
    
    # Verify book is borrowed
    assert sample_book.is_borrowed == True
    assert sample_book.borrowed_by == sample_member.member_id
    assert sample_book.book_id in sample_member.borrowed_books


def test_member_borrowing_limit(sample_member):
    # Member should be able to borrow initially
    assert sample_member.can_borrow() == True
    
    # Borrow 5 books (maximum)
    for i in range(5):
        sample_member.borrow_book(f"book_{i}")
    
    # Should not be able to borrow more
    assert sample_member.can_borrow() == False
    assert len(sample_member.borrowed_books) == 5


def test_section_capacity(sample_section):
    # Add books up to capacity
    for i in range(100):
        result = sample_section.add_book(f"book_{i}")
        assert result == True
    
    # Should be at capacity
    assert sample_section.is_at_capacity() == True
    
    # Should not be able to add more books
    result = sample_section.add_book("book_101")
    assert result == False

def test_redistribute_sections(library):
    # Add 3 members to 
    library.add_librarian(Librarian("Liam", "liam@loughystudios.com"))
    library.add_librarian(Librarian("Owen", "owen@loughystudios.com"))
    library.add_librarian(Librarian("Loughnane", "loughnane@loughystudios.com"))
    # check that they are in there
    assert len(library.librarians) == 3

    # Add sections to library
    library.add_section(Section("S1", 1, 100))
    library.add_section(Section("S2", 1, 100))
    library.add_section(Section("S3", 1, 100))
    library.add_section(Section("S4", 1, 100))
    library.add_section(Section("S5", 1, 100))
    library.add_section(Section("S6", 1, 100))
    library.add_section(Section("S7", 1, 100))
    library.add_section(Section("S8", 1, 100))
    
    # check they are in there and the amount is correct
    assert len(library.sections) == 8
    
    num_librarians = len(library.librarians)
    for i, section in enumerate(library.sections):
        librarian = library.librarians[i % num_librarians]
        librarian.assign_section(section)
    
    first_librarian = library.librarians[0]
    second_librarian = library.librarians[1]
    third_librarian = library.librarians[2]
    assert len(first_librarian.sections) == 3
    assert len(second_librarian.sections) == 3
    assert len(third_librarian.sections) == 2

    library.redistribute_section(first_librarian.employee_id)
    first_librarian = library.librarians[0]
    second_librarian = library.librarians[1]
    
    assert len(library.librarians) == 2
    assert len(first_librarian.sections) == 4
    assert len(second_librarian.sections) == 4


def test_get_all_librarians(library):
    # check for returning None
    all_librarians = library.get_all_librarians()
    assert all_librarians == []

    library.add_librarian(Librarian("l1", "e1"))
    library.add_librarian(Librarian("l2", "e2"))

    all_librarians = library.get_all_librarians()
    assert len(all_librarians) == 2

def test_get_all_sections_managed_by_a_librarian(library, sample_librarian, sample_section):
    library.add_librarian(sample_librarian)
    librarian_id = sample_librarian.employee_id
    all_sections = library.get_all_managed_sections(librarian_id)
    assert all_sections == []

    sample_librarian.assign_section(sample_section)
    all_sections = library.get_all_managed_sections(librarian_id)
    assert len(all_sections) == 1

def test_get_invalid_librarian(library):
    not_found = library.get_librarian("1")
    assert not_found is None
