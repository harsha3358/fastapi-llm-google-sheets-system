from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User
from sheets_service import read_users, add_user
from llm_service import generate_user_insight
import bcrypt

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users")
def get_users():
    data = read_users()
    return {"data": data[1:] if len(data) > 1 else []}

@app.post("/register")
def register(user: User):
    hashed = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    ).decode()

    # Generate AI insight
    insight = generate_user_insight(user.email, user.role)

    add_user(user.email, hashed, user.role, insight)

    return {"message": "User registered with AI insight"}