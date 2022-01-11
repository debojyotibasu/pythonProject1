import pytest

def get_data():
    return[
        ("rajat.s.das@gmail.com","pass@1234"),
        ("tanya.banerjee@yahoo.com","N0Pa$$"),
        ("abhijit.seal@gmail.com","aNoThErPaSs!@#$"),
        ("manisha.sarkar@hotmail.com","pA$$(*&^"),
        ("aritro.pal@yahoo.com","s0me0therPa$$")
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_doLogin(username,password):
    print(username, "===", password)