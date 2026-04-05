# GitHub Cloud Connector – AVENTISIA Assignment

## Objective

The purpose of this project is to develop a simple GitHub Cloud Connector that interacts with the GitHub REST API. The application demonstrates API integration, authentication, and the ability to perform basic repository operations through custom endpoints.

## Features

* Authentication using GitHub Personal Access Token (PAT)
* Fetch repositories of the authenticated user
* Create issues in a specified repository
* Retrieve issues from a repository

## Technology Stack

* Python
* FastAPI
* Requests library
* python-dotenv

## Project Setup

### Clone the Repository

git clone <your-repository-link>
cd AVENTISIA-assignment

### Install Dependencies

pip install fastapi uvicorn requests python-dotenv

### Environment Configuration

Create a `.env` file in the root directory and add the following:

GITHUB_TOKEN=your_personal_access_token

### Run the Application

python -m uvicorn main:app --reload

## API Endpoints

### 1. Fetch Repositories

Method: GET
Endpoint: /repos
Description: Returns the list of repositories for the authenticated user.

### 2. Create Issue

Method: POST
Endpoint: /create-issue
Description: Creates a new issue in the specified repository.

Request Body:
{
"owner": "your_username",
"repo": "your_repository_name",
"title": "Issue title",
"body": "Issue description"
}

### 3. List Issues

Method: GET
Endpoint: /issues
Description: Retrieves all issues from the specified repository.

Query Parameters:

* owner
* repo

Example:
/issues?owner=your_username&repo=your_repository_name

## Testing

The API can be tested using the FastAPI interactive documentation available at:
http://127.0.0.1:8000/docs

## Notes

* Ensure that the GitHub Personal Access Token has the required permissions (repo scope).
* The `.env` file should not be committed to version control.

## Conclusion

This project provides a basic implementation of integrating with the GitHub API using FastAPI. It can be extended further to include additional features such as pull request handling, repository management, and user-level analytics.
