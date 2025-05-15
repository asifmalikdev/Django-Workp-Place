from math import trunc

import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"


def get_posts():
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        print("Fetched posts:")
        for post in posts:
            print(f" { post["id"]} :  - {post['title']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


# POST request: Creating a new post
def create_post():
    new_post = {
        "title": "New Post Title",
        "body": "This is the content of the new post.",
        "userId": 1
    }
    response = requests.post(url, json=new_post)
    if response.status_code == 201:
        print("New post created successfully:")
        print(response.json())  # Printing the response of the created post
    else:
        print(f"Failed to create post. Status code: {response.status_code}")


# PUT request: Updating a post (replaces the entire post)
def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Post Title",
        "body": "This is the updated content of the post.",
        "userId": 1
    }
    response = requests.put(f"{url}/{post_id}", json=updated_post)
    if response.status_code == 200:
        print(f"Post {post_id} updated successfully:")
        print(response.json())
    else:
        print(f"Failed to update post. Status code: {response.status_code}")


# DELETE request: Deleting a post
def delete_post(post_id):
    response = requests.delete(f"{url}/{post_id}")
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")


# Main program
if __name__ == "__main__":
    # Fetching all posts (GET)
    print("Fetching all posts:")
    get_posts()

    # Creating a new post (POST)
    print("\nCreating a new post:")
    create_post()

    # Updating a post (PUT)
    post_id_to_update = 1  # Update post with ID 1
    print(f"\nUpdating post with ID {post_id_to_update}:")
    update_post(post_id_to_update)

    # Deleting a post (DELETE)
    post_id_to_delete = 2  # Delete post with ID 2
    print(f"\nDeleting post with ID {post_id_to_delete}:")
    delete_post(post_id_to_delete)

    print("Fetching all posts:")
    get_posts()

import requests

# NASA API endpoint for Astronomy Picture of the Day (APOD)
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)
data = response.json()

# Print the title and explanation of the image
print("Title:", data["title"])
print("Explanation:", data["explanation"])
print("Image URL:", data["url"])
class Solution(object):
    def searchInsert(self, nums, target):
        low, high=0, len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if target == nums[mid]:
                return mid
            elif target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return low

from math import trunc

import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"


def get_posts():
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        print("Fetched posts:")
        for post in posts:
            print(f" { post["id"]} :  - {post['title']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


# POST request: Creating a new post
def create_post():
    new_post = {
        "title": "New Post Title",
        "body": "This is the content of the new post.",
        "userId": 1
    }
    response = requests.post(url, json=new_post)
    if response.status_code == 201:
        print("New post created successfully:")
        print(response.json())  # Printing the response of the created post
    else:
        print(f"Failed to create post. Status code: {response.status_code}")


# PUT request: Updating a post (replaces the entire post)
def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Post Title",
        "body": "This is the updated content of the post.",
        "userId": 1
    }
    response = requests.put(f"{url}/{post_id}", json=updated_post)
    if response.status_code == 200:
        print(f"Post {post_id} updated successfully:")
        print(response.json())
    else:
        print(f"Failed to update post. Status code: {response.status_code}")


# DELETE request: Deleting a post
def delete_post(post_id):
    response = requests.delete(f"{url}/{post_id}")
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")


# Main program
if __name__ == "__main__":
    # Fetching all posts (GET)
    print("Fetching all posts:")
    get_posts()

    # Creating a new post (POST)
    print("\nCreating a new post:")
    create_post()

    # Updating a post (PUT)
    post_id_to_update = 1  # Update post with ID 1
    print(f"\nUpdating post with ID {post_id_to_update}:")
    update_post(post_id_to_update)

    # Deleting a post (DELETE)
    post_id_to_delete = 2  # Delete post with ID 2
    print(f"\nDeleting post with ID {post_id_to_delete}:")
    delete_post(post_id_to_delete)

    print("Fetching all posts:")
    get_posts()

import requests

# NASA API endpoint for Astronomy Picture of the Day (APOD)
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)
data = response.json()

# Print the title and explanation of the image
print("Title:", data["title"])
print("Explanation:", data["explanation"])
print("Image URL:", data["url"])
