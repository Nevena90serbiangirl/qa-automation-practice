import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/posts/1"

@pytest.mark.smoke
@pytest.mark.api
def test_delete_post():
    response = requests.delete(URL, timeout=10)

    assert response.status_code == 200
    assert response.json() == {}
    