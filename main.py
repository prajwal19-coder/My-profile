from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Mount static folders
app.mount("/css", StaticFiles(directory=BASE_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=BASE_DIR / "js"), name="js")
app.mount("/images", StaticFiles(directory=BASE_DIR / "images"), name="images")

# Function to load HTML files
def load_html(file_name: str):
    file_path = BASE_DIR / file_name
    return HTMLResponse(file_path.read_text(encoding="utf-8"))

# Routes
@app.get("/", response_class=HTMLResponse)
def home():
    return load_html("index.html")

@app.get("/projects", response_class=HTMLResponse)
def projects():
    return load_html("project.html")

@app.get("/experience", response_class=HTMLResponse)
def experience():
    return load_html("experience.html")
