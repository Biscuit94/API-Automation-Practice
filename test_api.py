import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
assert response.status_code == 200

data = response.json() # This will parse the JSON response into a Python dictionary
id_value = data["id"]
assert id_value == 1

title_value = data["title"]
assert title_value == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

response = requests.get("https://jsonplaceholder.typicode.com/posts/999")
assert response.status_code == 404

data = response.json()
#print(data)   This will print an empty dictionary since the post with id 999 does not exist
assert data == {}  # The response should be an empty dictionary for a non-existent post

response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
assert response.status_code == 200

data = response.json()
assert isinstance(data, list)  # The response should be a list of posts for userId=1

for post in data:
    assert post["userId"] == 1  # Each post should have userId equal to 1

response = requests.get("https://jsonplaceholder.typicode.com/posts")
assert response.status_code == 200
assert isinstance(response.json(), list)  # The response should be a list of all posts

data = response.json()
assert len(data) > 0  # There should be at least one post in the response