import allure
import pytest
from allure_commons.types import AttachmentType

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item=request.node
    driver=get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="doLogin", attachment_type=AttachmentType.PNG)

def get_data():
    return [
        ("rajat.s.das@gmail.com", "pass@1234"),
        ("tanya.banerjee@yahoo.com", "N0Pa$$"),
        ("abhijit.seal@gmail.com", "aNoThErPaSs!@#$"),
        ("manisha.sarkar@hotmail.com", "pA$$(*&^"),
        ("aritro.pal@yahoo.com", "s0me0therPa$$")
    ]


# def setup_function():
#     global driver
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     driver.get("https://www.facebook.com/")
#     driver.maximize_window()
#
#
# def teardown_function():
#     driver.quit()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_doLogin(username, password,get_browser):
    driver=get_browser
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys(password)
    # allure.attach(driver.get_screenshot_as_png(),name="doLogin",attachment_type=AttachmentType.PNG)
    # assert 1 == 2
