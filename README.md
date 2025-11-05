# Library Management System (LMS)

A REST API for managing library operations including books, members, sections, and librarians.

## Prerequisites

- Python 3.9 or higher
- [UV](https://github.com/astral-sh/uv) package manager

## Setup

### 1. Install UV (if not already installed)

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or via pip:**

```bash
pip install uv
```

### 2. Install project dependencies

```bash
# Sync all dependencies from pyproject.toml
uv sync
```

### 3. Run the application

```bash
# From project root
uv run python src/lms.py

# Or from src directory
cd src
uv run python lms.py
```

### 4. Access the Swagger UI

Open your browser and go to `http://127.0.0.1:7891`

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test files
uv run pytest tests/test_library_basic.py -v
uv run pytest tests/test_api_library.py -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=html
```

## Adding New Dependencies

```bash
# Add a new package
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a package
uv remove package-name
```

## Project Structure

```
library-management-system/
├── src/
│   ├── models/              # Data models
│   │   ├── book.py          # Book class
│   │   ├── member.py        # Member class
│   │   ├── librarian.py     # Librarian class
│   │   └── section.py       # Section class
│   ├── services/            # Business logic
│   │   └── library.py       # Library class managing all entities
│   ├── utils/               # Utility functions
│   │   └── library_json_utils.py  # JSON encoder for custom objects
│   └── lms.py              # Main Flask application with API endpoints
├── tests/                   # Test files
│   ├── test_library_basic.py
│   └── test_api_library.py
├── docs/                    # Documentation
│   └── Project_Description.md
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
└── README.md               # This file
```

## Development Workflow

1. **Make changes** to your code
2. **Run tests** to ensure everything works:
   ```bash
   uv run pytest tests/ -v
   ```
3. **Test the API** using Swagger UI at `http://127.0.0.1:7891` or with tools like Postman
4. **Commit your changes** to Git

## Your Task

Complete the implementation of all API endpoints as described in the project description document (`docs/Project_Description.md`).

### Focus Areas:

- ✅ Implementing all CRUD operations
- ✅ Adding business logic (borrowing limits, overdue calculations, etc.)
- ✅ Writing comprehensive tests
- ✅ Handling edge cases and errors
- ✅ Generating task schedules (cleaning, inventory, feeding)

### Key Features to Implement:

1. **Book borrowing/returning** with due date tracking
2. **Overdue fee calculation** ($0.50 per day)
3. **Member borrowing limits** (max 5 books)
4. **Section capacity management**
5. **Statistics endpoints** (books per genre, members with overdue books, etc.)
6. **Task generation** (cleaning schedules, inventory checks, overdue notifications)

## Useful Commands

```bash
# Start development server
uv run python src/lms.py

# Run tests in watch mode (requires pytest-watch)
uv run ptw tests/

# Format code (if you add ruff or black)
uv run ruff format src/ tests/

# Lint code
uv run ruff check src/ tests/

# Generate requirements.txt for compatibility
uv pip compile pyproject.toml -o requirements.txt
```

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`, make sure you're running from the project root:

```bash
cd /path/to/library-management-system
uv run python src/lms.py
```

### Port Already in Use

If port 7891 is busy, change it in `src/lms.py`:

```python
if __name__ == '__main__':
    lms_app.run(debug=False, port=7892)  # Use different port
```

### UV Not Found

Make sure UV is in your PATH after installation. Restart your terminal or run:

```bash
source ~/.bashrc  # or ~/.zshrc on macOS
```

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTX Documentation](https://flask-restx.readthedocs.io/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Pytest Documentation](https://docs.pytest.org/)

---

Good luck! 📚 Happy coding!
