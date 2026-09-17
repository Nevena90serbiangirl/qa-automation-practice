def verify_post(post):
    assert post["id"] == 1, "Expected post ID to be the number 1"

    assert isinstance(post["title"], str), "Expected title to be text"

    assert post["title"] != "", "Expected a non-empty title"

    print("PASSED: Post data is valid.")


response_data = {
    "userId": 1,
    "id": 1,
    "title": "My first API practice",
    "body": "Learning to check response data."
}

verify_post(response_data)