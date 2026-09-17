def verify_result(test_name, actual, expected):
    print(f"Running: {test_name}")

    assert actual == expected, (
        f"FAILED: Expected '{expected}', but received '{actual}'"
    )

    print("PASSED")


verify_result(
    "Successful login message",
    "Welcome, Nevena!",
    "Welcome, Nevena!"
)
verify_result(
    "Profile name",
    "Nevena Suknovic",
    "Nevena Suknovic"
)