BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_with_api_client(api_client):
    response = api_client.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert isinstance(post["title"], str)
    assert post["title"] != ""