import pytest

@pytest.fixture(scope='module')
def setup():
    print("Registering DB Connection")

    yield
    print("Closing DB Connection")

@pytest.fixture(scope='function')
def before():
    print("Launching Browser")

    yield
    print("Closing Browser")

# def test_doLogin(setup, before):
#     print("Executing Login Test")
#
# def test_userRegistration(setup,before):
#     print("Executing User Registration Test")

@pytest.mark.usefixtures("setup", "before")
def test_doLogin():
    print("Executing Login Test")

@pytest.mark.usefixtures("setup", "before")
def test_userRegistration():
    print("Executing User Registration Test")