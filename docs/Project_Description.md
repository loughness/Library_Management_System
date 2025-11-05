# Library Management System (LMS)

**Suggested Timeline:** 2-3 weeks  
**Difficulty Level:** Intermediate

---

## Project Overview

Imagine you're building software for managing a modern library. The software will be used by librarians to manage books, track borrowing/returns, monitor member activities, and plan maintenance tasks.

This project focuses on implementing a **REST API** using Flask. You'll practice object-oriented programming, API design, and automated testing. The front-end is not part of this exercise - you can test using Postman, Python requests, or the Swagger UI that comes with Flask-RESTX.

**Design Goal:** Create classes and objects that allow for easy future extensions (e.g., adding e-books, audiobooks, or study rooms).

---

## Core Functionality

### 1. Book Management

- Add/remove books to/from the library
- Each book has: `book_id`, `isbn`, `title`, `author`, `genre`, `publication_year`
- Books belong to a section (e.g., "Fiction Floor 2", "Science Floor 1")
- Track borrowing history: who borrowed it, when borrowed, when returned
- Track if a book is currently available or checked out

### 2. Member Management

- Add/remove members from the system
- Each member has: `member_id`, `name`, `email`, `phone`, `membership_date`
- Track books currently borrowed by each member
- Members can borrow maximum 5 books at a time
- When a member is removed, they must return all books first

### 3. Librarian Management

- Add/remove librarians from the system
- Each librarian has: `employee_id`, `name`, `email`, `section_assigned`
- Each librarian is responsible for one or more sections
- When a librarian leaves, reassign their sections to another librarian

### 4. Section Management

- Books are organized into sections (e.g., Fiction, Science, History, Children's)
- Each section has: `section_id`, `name`, `floor`, `capacity` (max number of books)
- Track when each section was last cleaned
- Sections can contain multiple books, potentially from different genres

### 5. Borrowing & Returning

- Members can borrow available books
- Loan period: 14 days
- Track the due date for each borrowed book
- When a book is returned, calculate if it's overdue
- Late fee: $0.50 per day overdue

### 6. Task Scheduling

- **Section Cleaning Plan**: Sections must be cleaned every 7 days
- **Inventory Check Plan**: Books must be inventoried every 30 days
- **Overdue Notification Plan**: Generate list of overdue books and members to contact

---

## API Endpoints to Implement

### Book Endpoints

| Method | URL Path                  | Description                                                                                                                                    |
| ------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| POST   | `/book`                   | Add a new book (params: `isbn`, `title`, `author`, `genre`, `publication_year`) Returns book details including `book_id`                       |
| GET    | `/book/<book_id>`         | Get details of a specific book                                                                                                                 |
| GET    | `/books`                  | Get list of all books with their details                                                                                                       |
| DELETE | `/book/<book_id>`         | Delete a book (only if not currently borrowed)                                                                                                 |
| POST   | `/book/<book_id>/section` | Assign a book to a section (params: `section_id`)                                                                                              |
| POST   | `/book/<book_id>/borrow`  | Borrow a book (params: `member_id`). Track borrow date and calculate due date                                                                  |
| POST   | `/book/<book_id>/return`  | Return a book. Calculate if overdue and any late fees                                                                                          |
| GET    | `/books/available`        | Get list of all available (not borrowed) books                                                                                                 |
| GET    | `/books/overdue`          | Get list of all overdue books with member details                                                                                              |
| GET    | `/books/stats`            | Get statistics: <br>- Total books per genre<br>- Total books per section<br>- Average books per member<br>- Most popular books (most borrowed) |

### Member Endpoints

| Method | URL Path                      | Description                                                                                             |
| ------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| POST   | `/member`                     | Add a new member (params: `name`, `email`, `phone`)                                                     |
| GET    | `/member/<member_id>`         | Get member details                                                                                      |
| GET    | `/members`                    | Get list of all members                                                                                 |
| DELETE | `/member/<member_id>`         | Delete a member (must return all books first)                                                           |
| GET    | `/member/<member_id>/books`   | Get list of books currently borrowed by member                                                          |
| GET    | `/member/<member_id>/history` | Get borrowing history of a member                                                                       |
| GET    | `/members/stats`              | Get statistics:<br>- Total active members<br>- Members with overdue books<br>- Average books per member |

### Section Endpoints

| Method | URL Path                      | Description                                                                                             |
| ------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| POST   | `/section`                    | Add a new section (params: `name`, `floor`, `capacity`)                                                 |
| GET    | `/section/<section_id>`       | Get section details                                                                                     |
| GET    | `/sections`                   | Get list of all sections                                                                                |
| DELETE | `/section/<section_id>`       | Delete a section (move books to another section first)                                                  |
| GET    | `/section/<section_id>/books` | Get all books in a section                                                                              |
| POST   | `/section/<section_id>/clean` | Mark section as cleaned (track date/time)                                                               |
| GET    | `/sections/stats`             | Get statistics:<br>- Books per section<br>- Sections at/over capacity<br>- Utilization rate per section |

### Librarian Endpoints

| Method | URL Path                                         | Description                                   |
| ------ | ------------------------------------------------ | --------------------------------------------- |
| POST   | `/librarian`                                     | Add a new librarian (params: `name`, `email`) |
| GET    | `/librarian/<librarian_id>`                      | Get librarian details                         |
| GET    | `/librarians`                                    | Get list of all librarians                    |
| DELETE | `/librarian/<librarian_id>`                      | Delete a librarian (reassign sections first)  |
| POST   | `/librarian/<librarian_id>/section/<section_id>` | Assign a section to a librarian               |
| GET    | `/librarian/<librarian_id>/sections`             | Get all sections managed by a librarian       |

### Task Management Endpoints

| Method | URL Path               | Description                                                                                     |
| ------ | ---------------------- | ----------------------------------------------------------------------------------------------- |
| GET    | `/tasks/cleaning`      | Generate cleaning schedule for all sections (show next cleaning date and responsible librarian) |
| GET    | `/tasks/inventory`     | Generate inventory check schedule (show next check date per section)                            |
| GET    | `/tasks/notifications` | Generate list of overdue books and members to notify                                            |

---

## Technical Requirements

### 1. Implementation

- Use **Flask** and **Flask-RESTX** for API implementation
- Use proper object-oriented design (classes for Book, Member, Librarian, Section)
- Each HTTP method should return appropriate JSON responses
- Handle errors gracefully (e.g., book not found, member borrowing limit exceeded)

### 2. Data Tracking

- Track dates using `datetime` module
- Calculate due dates (14 days from borrow date)
- Calculate overdue days and late fees
- Track cleaning dates for sections
- Track borrowing history

### 3. Business Rules

- Members can borrow maximum 5 books at a time
- Books can only be deleted if not currently borrowed
- Members can only be deleted if they have no borrowed books
- Loan period is 14 days
- Late fee is $0.50 per day
- Sections must be cleaned every 7 days
- Inventory checks every 30 days

### 4. Testing

- Write comprehensive test cases using **pytest**
- Test all CRUD operations
- Test business logic (borrowing limits, overdue calculations, etc.)
- Test edge cases (borrowing unavailable book, deleting member with books, etc.)
- Create automated test scenarios simulating library operations

### Example Test Scenarios:

1. Add several books and members
2. Borrow books for different members
3. Return some books on time, some overdue
4. Check statistics
5. Generate cleaning and inventory schedules
6. Test member borrowing limit
7. Test section capacity
8. Clean sections and verify tracking

---

## Starter Code Structure

You'll receive starter files similar to the zoo project:

- `lms.py` - Main Flask application with some example endpoints
- `library.py` - Library class to manage all entities
- `book.py` - Book class
- `member.py` - Member class
- `librarian.py` - Librarian class
- `section.py` - Section class
- `library_json_utils.py` - JSON encoder for custom objects
- Test files to get you started

---

## Submission Guidelines

1. Create a GitHub repository for your project
2. Implement all required endpoints
3. Write comprehensive tests
4. Include a README.md with:
   - How to run the application
   - How to run tests
   - Any additional features you implemented
5. Make sure your code is well-commented and follows good practices

---

## Extensions (Optional Challenges)

If you finish early and want more practice:

1. Add book reservation system (reserve a book that's currently borrowed)
2. Add different membership tiers (basic, premium) with different borrowing limits
3. Add book ratings and reviews by members
4. Add study room booking system
5. Add email notification simulation for overdue books
6. Add book renewal option (extend due date)
7. Implement pagination for large lists
8. Add search functionality (search books by title, author, genre)

---

## Learning Objectives

By completing this project, you will practice:

- REST API design and implementation
- Object-oriented programming in Python
- Managing relationships between objects
- Date/time calculations
- Writing automated tests
- Handling business logic and validation
- JSON serialization
- Error handling in APIs
