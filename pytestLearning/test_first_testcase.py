import pytest

def setup_module(module):
    print("Registering DB Connection")

def teardown_module(module):
    print("Closing DB Connection")

def setup_function(function):
    print("Launching Browser")

def teardown_function(function):
    print("Closing Browser")

def test_doLogin():
    # print("Launching Browser")
    print("Executing Login Test")
    # print("Closing Browser")

def test_userRegistration():
    # print("Launching Browser")
    print("Executing User Registration Test")
    # print("Closing Browser")