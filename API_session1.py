import requests

# -------------------------------
# Task 1: Manual DevTools Observation
# -------------------------------
def task1_devtools():
    print("\n--- Task 1: DevTools Observation ---")
    print("Open Instagram or Flipkart in browser → F12 → Network → Refresh.")
    print("Note down: Request URL, HTTP Method, Status Code.")
    print("Example: URL=https://www.flipkart.com/api/... , Method=GET , Status=200")


# -------------------------------
# Task 2: GET request with Postman (Python equivalent)
# -------------------------------
def task2_get_request():
    print("\n--- Task 2: GET Request ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    posts = response.json()
    print("First Post Title:", posts[0]["title"])


# -------------------------------
# Task 3: JSON object for Zomato-style restaurant
# -------------------------------
def task3_post_request():
    print("\n--- Task 3: POST Request ---")
    restaurant = {
        "name": "Spice Villa",
        "cuisine": "Indian",
        "rating": 4.5
    }
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=restaurant)
    print("Status Code:", response.status_code)
    print("Response:", response.json())


# -------------------------------
# Task 4: PUT vs PATCH
# -------------------------------
def task4_put_patch():
    print("\n--- Task 4: PUT vs PATCH ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # PUT replaces entire resource
    put_data = {
        "id": 1,
        "title": "Updated Title",
        "body": "Replaced full content",
        "userId": 1
    }
    put_response = requests.put(url, json=put_data)
    print("PUT Response:", put_response.json())

    # PATCH updates only specific field
    patch_data = {"title": "Patched Title"}
    patch_response = requests.patch(url, json=patch_data)
    print("PATCH Response:", patch_response.json())

    print("Example: PUT = update full profile, PATCH = update only phone number.")


# -------------------------------
# Task 5: Missing Headers
# -------------------------------
def task5_missing_headers():
    print("\n--- Task 5: Missing Headers ---")
    url = "https://jsonplaceholder.typicode.com/posts"

    # Without Content-Type header (sending raw text)
    response = requests.post(url, data='{"name":"Test"}')
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    print("Explanation: Without Content-Type → server may reject JSON.")
    print("Without Authorization → server returns 401 Unauthorized.")


# -------------------------------
# Main Runner
# -------------------------------
if __name__ == "__main__":
    task1_devtools()
    task2_get_request()
    task3_post_request()
    task4_put_patch()
    task5_missing_headers()
