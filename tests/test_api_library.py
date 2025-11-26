import pytest
import requests
import json


@pytest.fixture
def base_url():
    return "http://127.0.0.1:7891"


@pytest.fixture
def sample_book_data():
    return {
        'isbn': '978-0-123456-78-9',
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Fiction',
        'publication_year': 2020
    }

@pytest.fixture
def sample_librarian():
    return {
        'name': 'Liam',
        'email': 'liam@loughystudios.com',
    }


def test_add_and_get_book(base_url, sample_book_data):
    # Add a book
    response = requests.post(f"{base_url}/book", data=sample_book_data)
    assert response.status_code == 200
    book_data = response.json()
    book_id = book_data['book_id']
    
    # Get the book
    response = requests.get(f"{base_url}/book/{book_id}")
    assert response.status_code == 200
    retrieved_book = response.json()
    assert retrieved_book['title'] == sample_book_data['title']


def test_get_all_books(base_url, sample_book_data):
    # Add a book
    requests.post(f"{base_url}/book", data=sample_book_data)
    
    # Get all books
    response = requests.get(f"{base_url}/books")
    assert response.status_code == 200
    books = response.json()
    assert len(books) >= 1


def test_add_and_get_librarian(base_url, sample_librarian):
    response = requests.post(f"{base_url}/librarian", data=sample_librarian)
    assert response.status_code == 200
    librarian_data = response.json()
    librarian_id = librarian_data['employee_id']

    response = requests.get(f"{base_url}/librarian/{librarian_id}")
    assert response.status_code == 200
    retrieved_librarian = response.json()
    assert retrieved_librarian['name'] == sample_librarian['name']