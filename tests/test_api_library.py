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

@pytest.fixture
def sample_section():
    return {
        "name": "Technology",
        "floor": 1,
        "capacity": 100,
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

def test_add_section_assign_section_and_get_all_managed_sections_by_librarian_and_delete_section(
        base_url, 
        sample_librarian, 
        sample_section
        ):
    
    response = requests.post(f"{base_url}/librarian", data=sample_librarian)
    assert response.status_code == 200
    librarian_data = response.json()
    librarian_id = librarian_data['employee_id']

    # check that librarian does not have any sections
    response = requests.get(f"{base_url}/librarian/{librarian_id}/sections")
    all_sections_data = response.json()
    assert all_sections_data == []

    # add section to library
    response = requests.post(f"{base_url}/section", data=sample_section)
    assert response.status_code == 200
    section_data = response.json()
    section_id = section_data["section_id"]

    # assign librarian the section
    response = requests.post(f"{base_url}/librarian/{librarian_id}/section/{section_id}")
    assert response.status_code == 200

    # check that librarian does not have any sections
    response = requests.get(f"{base_url}/librarian/{librarian_id}/sections")
    all_sections_data = response.json()
    assert len(all_sections_data) == 1

    # delete section | check librarian has no sections | check library does not have section
    response = requests.delete(f"{base_url}/section/{section_id}")
    assert response.status_code == 200
    response = requests.get(f"{base_url}/librarian/{librarian_id}/sections")
    all_sections_data = response.json()
    assert all_sections_data == []
    #TODO: Catch errors correctly
    # response = requests.get(f"{base_url}/section/{section_id}")
    # response_data = response.json()
    # assert response_data == "section_not_found"


def test_get_section_details(base_url, sample_section):
    response = requests.post(f"{base_url}/section", data=sample_section)
    assert response.status_code == 200
    section_data = response.json()
    section_id = section_data["section_id"]

    response = requests.get(f"{base_url}/section/{section_id}")
    assert response.status_code == 200
    section_details = response.json()
    assert section_details["name"] == "Technology"
    assert section_details["floor"] == 1