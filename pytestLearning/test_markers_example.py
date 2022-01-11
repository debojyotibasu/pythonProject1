import pytest

@pytest.mark.functional
def test_doLogin():
    print("Executing Login Test")

@pytest.mark.regression
def test_userRegistration():
    print("Executing User Registration Test")

@pytest.mark.functional
def test_composeEmail():
    print("Executing Compose Email Test")

@pytest.mark.skip
def test_skip():
    print("Skipping Test")