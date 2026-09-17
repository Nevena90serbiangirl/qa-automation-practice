import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_posts_belong_to_requested_user(user_id):
    response = requests.get(
        URL,
        params={"userId": user_id},
        timeout=10
    )

    assert response.status_code == 200
    
    
    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == user_id
        assert isinstance(post["title"], str)
        assert post["title"] != ""