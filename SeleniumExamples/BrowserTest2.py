from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# For Chrome Browser
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# For Firefox Browser
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# For Edge Browser
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://www.amazon.in/")
driver.maximize_window()
title = driver.title
print("Page title: {}".format(title))
assert "Amazon.in" in title
driver.quit()