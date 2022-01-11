import pytest

def test_validate_title():
    expected_title = "google.com"
    actual_title = "gmail.com"
    title = "This is gmail website"

    # if actual_title == expected_title:
    #     print("Test case pass")
    # else:
    #     print("Test case fail")

    print("Begin test")
    assert actual_title == expected_title, "Titles are not matching"
    assert "gmails" in title, '"gmail" does not exists in title'
    assert False, "Forcefully failing the test"
    print("End test")