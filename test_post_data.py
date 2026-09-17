response_data = {
    "userId": 1,
    "id": 1,
    "title": "My first API practice",
    "body": "Learning to check response data."
}


def test_post_id():
    assert response_data["id"] == 1
    


def test_title_is_text():
    assert isinstance(response_data["title"], str)


def test_title_is_not_empty():
    assert response_data["title"] != ""