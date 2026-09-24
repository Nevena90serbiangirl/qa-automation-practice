BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_response_quality(api_client):
    response = api_client.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    print(
        "Response time:",
        response.elapsed.total_seconds(),
        "seconds"
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 3

    response_data = response.json()

    assert response_data["id"] == 1