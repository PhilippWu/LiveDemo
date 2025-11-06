from fastapi import FastAPI

app = FastAPI(title="Minimal FastAPI Service")


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/todos")
def get_todos():
    """Get static list of todos."""
    return [{"id": 1, "title": "demo"}]
