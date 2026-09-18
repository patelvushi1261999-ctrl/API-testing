import requests

# -------------------------------
# Task 1: GET request to /posts/1
# -------------------------------
def task1_get_post():
    print("\n--- Task 1 ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Full JSON Response:", response.json())


# -------------------------------
# Task 2: GET request to /users
# -------------------------------
def task2_get_users():
    print("\n--- Task 2 ---")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200, "Expected status code 200"
    users = response.json()
    assert isinstance(users, list), "Response body is not an array"
    assert len(users) >= 5, "Expected at least 5 users"
    print("Number of users:", len(users))


# -------------------------------
# Task 3: GET comments for postId=1
# -------------------------------
def task3_get_comments():
    print("\n--- Task 3 ---")
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    response = requests.get(url)
    comments = response.json()
    for idx, comment in enumerate(comments, start=1):
        assert comment.get("email"), f"Comment {idx} has empty email"
    print("All comments have non-empty email fields.")


# -------------------------------
# Task 4: GET album /albums/3
# -------------------------------
def task4_get_album():
    print("\n--- Task 4 ---")
    url = "https://jsonplaceholder.typicode.com/albums/3"
    response = requests.get(url)
    album = response.json()
    assert "userId" in album, "Response missing 'userId'"
    assert isinstance(album["userId"], int), "'userId' is not a number"
    print("Album contains userId:", album["userId"])


# -------------------------------
# Main Runner
# -------------------------------
if __name__ == "__main__":
    task1_get_post()
    task2_get_users()
    task3_get_comments()
    task4_get_album()
