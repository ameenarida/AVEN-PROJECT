from fastapi import FastAPI
from github_service import get_repos

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AVENTISIA GitHub Connector Running"}

@app.get("/repos")
def fetch_repos():
    return get_repos()

from fastapi import Body
from github_service import create_issue

@app.post("/create-issue")
def create_issue_api(
    owner: str = Body(...),
    repo: str = Body(...),
    title: str = Body(...),
    body: str = Body(...)
):
    return create_issue(owner, repo, title, body)    

from github_service import list_issues

@app.get("/issues")
def get_issues(owner: str, repo: str):
    return list_issues(owner, repo)