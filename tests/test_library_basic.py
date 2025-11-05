import pytest
from book import Book
from member import Member
from src.section import Section
from librarian import Librarian
from library import Library


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