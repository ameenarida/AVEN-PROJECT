# GitHub Cloud Connector – AVENTISIA Assignment

## Objective
The purpose of this project is to develop a simple GitHub Cloud Connector that interacts with the GitHub REST API. It demonstrates API integration, authentication, and basic repository operations.

## Features
- Authentication using GitHub Personal Access Token (PAT)
- Fetch repositories
- Create issues
- Retrieve issues

## Technology Stack
- Python
- FastAPI
- Requests
- python-dotenv

## Installation
pip install -r requirements.txt

## Project Setup
Clone repository:
git clone https://github.com/ameenarida/AVEN-PROJECT
cd AVENTISIA-assignment

Install dependencies:
pip install fastapi uvicorn requests python-dotenv

Create .env file:
GITHUB_TOKEN=your_personal_access_token

Run application:
python -m uvicorn main:app --reload

## API Endpoints

### Fetch Repositories
GET /repos  
Returns user repositories

### Create Issue
POST /create-issue  
Creates a new issue  

Request body:
{
  "owner": "your_username",
  "repo": "your_repository_name",
  "title": "Issue title",
  "body": "Issue description"
}

### List Issues
GET /issues  
Query: owner, repo  

Example:
/issues?owner=your_username&repo=your_repository_name

## Testing
Open:
http://127.0.0.1:8000/docs

## Notes
- Keep .env file private
- Ensure token has repo permission

## Conclusion
This project shows basic GitHub API integration using FastAPI with features like fetching repositories and managing issues.