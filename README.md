# LiveDemo

A minimal FastAPI service with tests and CI/CD.

## Features

- **GET /health** - Health check endpoint that returns `{"status": "ok"}`
- **GET /todos** - Returns a static list of todos: `[{"id": 1, "title": "demo"}]`

## Project Structure

```
.
├── src/
│   └── fastapi_app/
│       ├── __init__.py
│       └── main.py          # FastAPI application
├── tests/
│   └── test_main.py         # pytest tests
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI
├── pyproject.toml           # Project configuration
└── README.md
```

## Setup

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/PhilippWu/LiveDemo.git
cd LiveDemo
```

2. Install the package with dependencies:
```bash
pip install -e .
```

3. For development (with test dependencies):
```bash
pip install -e ".[test]"
```

## Running the Application

Start the FastAPI server using uvicorn:

```bash
uvicorn src.fastapi_app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

### Testing Endpoints

Using curl:

```bash
# Health check
curl http://localhost:8000/health

# Get todos
curl http://localhost:8000/todos
```

## Running Tests

Run all tests with pytest:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

## CI/CD

The project includes a GitHub Actions workflow that:
- Runs on Python 3.11
- Installs dependencies
- Executes pytest on every push and pull request to the main branch

## License

This project is provided as-is for demonstration purposes.