import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_repos():
    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()

def create_issue(owner, repo, title, body):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        return {"error": response.json()}

    return response.json()    

def list_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()