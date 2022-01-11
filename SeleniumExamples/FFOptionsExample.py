import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

# Method 1
# firefox_options = Options()

# Method 2
firefox_options = webdriver.FirefoxOptions()

firefox_options.set_preference('dom.webnotifications.enabled', False)
# firefox_options.headless = True

# For Firefox Browser
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

# driver.get("https://www.sastasundar.com/")
driver.get("https://www.eenadu.net/")
driver.maximize_window()
time.sleep(2)
print(driver.title)