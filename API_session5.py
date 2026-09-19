import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# -------------------------------
# Task 1: POST - Create new post
# -------------------------------
def task1_post_create():
    print("\n--- Task 1: POST Create ---")
    payload = {"title": "My Custom Title", "body": "This is my custom body"}
    response = requests.post(BASE_URL, json=payload)
    print("Status Code:", response.status_code)
    data = response.json()
    print("Response JSON:", data)
    post_id = data.get("id")
    print("Created Post ID:", post_id)
    return post_id


# -------------------------------
# Task 2: PUT - Update full post
# -------------------------------
def task2_put_update(post_id):
    print("\n--- Task 2: PUT Update ---")
    payload = {"id": post_id, "title": "Updated Title", "body": "Updated Body"}
    response = requests.put(f"{BASE_URL}/{post_id}", json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


# -------------------------------
# Task 3: PATCH - Update only title
# -------------------------------
def task3_patch_update(post_id):
    print("\n--- Task 3: PATCH Update ---")
    payload = {"title": "Patched Title"}
    response = requests.patch(f"{BASE_URL}/{post_id}", json=payload)
    print("Status Code:", response.status_code)
    data = response.json()
    print("Response JSON:", data)
    if "body" in data:
        print("Body remains unchanged:", data["body"])


# -------------------------------
# Task 4: DELETE - Remove post
# -------------------------------
def task4_delete(post_id):
    print("\n--- Task 4: DELETE ---")
    response = requests.delete(f"{BASE_URL}/{post_id}")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # Try to fetch deleted post
    get_response = requests.get(f"{BASE_URL}/{post_id}")
    print("GET after DELETE Status:", get_response.status_code)
    print("GET after DELETE Response:", get_response.text)


# -------------------------------
# Task 5: Validate CRUD responses
# -------------------------------
def task5_validate(post_id):
    print("\n--- Task 5: Validation Summary ---")

    # POST
    post_resp = requests.post(BASE_URL, json={"title": "Test", "body": "Body"})
    print("POST → Status:", post_resp.status_code, "Fields:", post_resp.json().keys())

    # PUT
    put_resp = requests.put(f"{BASE_URL}/{post_id}", json={"id": post_id, "title": "PutTest", "body": "PutBody"})
    print("PUT → Status:", put_resp.status_code, "Fields:", put_resp.json().keys())

    # PATCH
    patch_resp = requests.patch(f"{BASE_URL}/{post_id}", json={"title": "PatchTest"})
    print("PATCH → Status:", patch_resp.status_code, "Fields:", patch_resp.json().keys())

    # DELETE
    delete_resp = requests.delete(f"{BASE_URL}/{post_id}")
    print("DELETE → Status:", delete_resp.status_code, "Response:", delete_resp.text)


# -------------------------------
# Main Runner
# -------------------------------
if __name__ == "__main__":
    new_post_id = task1_post_create()
    task2_put_update(new_post_id)
    task3_patch_update(new_post_id)
    task4_delete(new_post_id)
    task5_validate(new_post_id)
