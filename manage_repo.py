def comment_on_issue(issue_number, comment):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    data = {
        "body": comment
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Comment added successfully.")
    else:
        print(f"Failed to add comment: {response.status_code}, {response.json()}")

# Example usage
# Uncomment to use these functions
# create_issue("Test Issue", "This is a test issue created by AI.")
# merge_pull_request(1)  # Assuming pull request number 1
# comment_on_issue(1, "This is a test comment from AI.")
