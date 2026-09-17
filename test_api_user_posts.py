import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def test_posts_for_user_one():
    parameters = {
        "userId": 1
    }

    response = requests.get(
        URL,
        params=parameters,
        timeout=10
    )
    
    print(response.url)

    assert response.status_code == 200
    
    
    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0
    
    for post in posts:
        assert post["userId"] == 1
        assert isinstance(post["title"], str)
        assert post["title"] != ""