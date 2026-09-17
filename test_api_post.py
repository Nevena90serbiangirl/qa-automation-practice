import requests


URL = "https://jsonplaceholder.typicode.com/posts/1"


def test_status_code():
    response = requests.get(URL, timeout=10)

    assert response.status_code == 200
    
    
def test_post_data():
        response = requests.get(URL, timeout=10)
        response_data = response.json()

        assert response_data["id"] == 1
        assert isinstance(response_data["title"], str)
        assert response_data["title"] != ""