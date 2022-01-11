import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)
    return rep

# @pytest.fixture(scope="function")
# # @pytest.fixture(scope="session")
# def chrome_browser():
#     global driver
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     driver.get("https://www.facebook.com/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    remote_url="http://localhost:4444/wd/hub"
    if request.param == "chrome":
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url,desired_capabilities={"browserName":"chrome"})
    if request.param == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})

    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()