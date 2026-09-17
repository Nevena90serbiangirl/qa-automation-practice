def verify_post(post):
    print(f"Checking post ID: {post['id']}")

    assert isinstance(post["title"], str), "Expected title to be text"

    assert post["title"] != "", (
        f"Post {post['id']}: Expected a non-empty title"
    )

    print("PASSED")


posts = [
    {"id": 1, "title": "First post"},
    {"id": 2, "title": "Second post"},
    {"id": 3, "title": "Third post"}
]

for post in posts:
    verify_post(post)

print("Finished: all posts passed.")