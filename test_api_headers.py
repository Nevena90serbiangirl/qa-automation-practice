import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/posts/1"


@pytest.mark.api
def test_post_response_headers():
    response = requests.get(URL, timeout=10)

    assert response.status_code == 200

    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type

    response_data = response.json()
    required_keys = {"userId", "id", "title", "body"}

    assert required_keys.issubset(response_data)