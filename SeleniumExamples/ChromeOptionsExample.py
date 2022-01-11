import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Method 1
chrome_options = Options()

# Method 2
# chrome_options = webdriver.ChromeOptions

prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.headless = True

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

driver.get("https://www.sastasundar.com/")
# driver.get("https://www.eenadu.net/")
driver.maximize_window()
time.sleep(2)
print(driver.title)