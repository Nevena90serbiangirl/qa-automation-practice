import requests


URL = "https://jsonplaceholder.typicode.com/posts/1"


def test_update_post_with_put():
    updated_post = {
        "id": 1,
        "title": "Updated QA automation post",
        "body": "This post was completely updated using PUT.",
        "userId": 1
    }
    
    
    response = requests.put(
        URL,
        json=updated_post,
        timeout=10
    )

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["id"] == updated_post["id"]
    assert response_data["title"] == updated_post["title"]
    assert response_data["body"] == updated_post["body"]
    assert response_data["userId"] == updated_post["userId"]
    
def test_update_post_with_patch():
    partial_update = {
        "title": "Partially updated QA post"
    }
    response = requests.patch(
        URL,
        json=partial_update,
        timeout=10
    )

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["title"] == partial_update["title"]
    assert response_data["id"] == 1
    assert "body" in response_data
    assert "userId" in response_data