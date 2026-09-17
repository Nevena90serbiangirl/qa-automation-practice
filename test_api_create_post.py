import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def test_create_post():
    new_post = {
        "title": "My QA automation practice",
        "body": "Learning how to send a POST request.",
        "userId": 1
    }
    response = requests.post(
        URL,
        json=new_post,
        timeout=10
    )
    assert response.status_code == 201
    created_post = response.json()
    
    assert created_post["title"] == new_post["title"]
    assert created_post["body"] == new_post["body"]
    assert created_post["userId"] == new_post["userId"]
    assert "id" in created_post