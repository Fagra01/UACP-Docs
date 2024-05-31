import os
import requests

# Get the GitHub token from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "Universal-AI-Collaboration-Platform"
REPO_NAME = "UACP"

# Set up headers for GitHub API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_issue(title, body):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Issue created successfully.")
    else:
        print(f"Failed to create issue: {response.status_code}, {response.json()}")

def merge_pull_request(pull_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pull_number}/merge"
    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        print("Pull request merged successfully.")
    else:
        print(f"Failed to merge pull request: {response.status_code}, {response.json()}")

# Example usage
# Uncomment the lines below to use these functions
# create_issue("Test Issue", "This is a test issue created by AI.")
# merge_pull_request(1)  # Assuming pull request number 1
