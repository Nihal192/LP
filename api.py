import requests

# Base URL for JSONPlaceholder
url = "https://jsonplaceholder.typicode.com"

# Example: Fetching a list of posts
response = requests.get(f"{url}/posts")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    posts = response.json()
    
    # Print the first post as an example
    print("First Post:")
    print(f"ID: {posts[0]['id']}")
    print(f"Title: {posts[0]['title']}")
    print(f"Body: {posts[0]['body']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Example: Fetching a specific post by ID
post_id = 1
response = requests.get(f"{url}/posts/{post_id}")

if response.status_code == 200:
    post = response.json()
    print("\nPost Details:")
    print(f"ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
else:
    print(f"Failed to retrieve post: {response.status_code}")

# Example: Fetching a list of comments for a specific post
response = requests.get(f"{url}/posts/{post_id}/comments")

if response.status_code == 200:
    comments = response.json()
    print(f"\nComments for Post {post_id}:")
    for comment in comments:
        print(f"Comment ID: {comment['id']}")
        print(f"Name: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Body: {comment['body']}")
        print("---")
else:
    print(f"Failed to retrieve comments: {response.status_code}")
