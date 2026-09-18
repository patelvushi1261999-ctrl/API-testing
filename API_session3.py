import pytest

# -------------------------------
# Task 1: Verify installation
# -------------------------------
# (Manual step, not code)
# Run in terminal after installing:
#   pytest --help
# Confirm Playwright options appear.

# -------------------------------
# Task 2: Project setup
# -------------------------------
# Folder: api_testing_demo
# File: test_api_status.py (this file)

# -------------------------------
# Task 3 & 4: GET request and count posts
# -------------------------------
def test_api_status(request):
    # Send GET request
    response = request.get("https://jsonplaceholder.typicode.com/posts")
    # Assert status code
    assert response.status == 200
    # Parse JSON and count posts
    posts = response.json()
    print("Number of posts returned:", len(posts))


# -------------------------------
# Task 5: POST request with sample JSON body
# -------------------------------
def test_api_post(request):
    payload = {
        "title": "Sample Title",
        "body": "Demo body content"
    }
    # Send POST request
    response = request.post("https://jsonplaceholder.typicode.com/posts", data=payload)
    # Assert status code
    assert response.status == 201
    # Print response JSON
    print("POST Response JSON:", response.json())
