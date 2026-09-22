import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/posts/999999"


@pytest.mark.api
def test_missing_post_returns_404():
    response = requests.get(URL, timeout=10)

    assert response.status_code == 404