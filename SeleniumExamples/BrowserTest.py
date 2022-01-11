from selenium import webdriver

# For Chrome Browser
# driver = webdriver.Chrome(executable_path="D:\\SeleniumNewSW\\chromedriver.exe")

# For Firefox Browser
# driver = webdriver.Firefox(executable_path="D:\\SeleniumNewSW\\geckodriver.exe")

# For Edge Browser
driver = webdriver.Edge(executable_path="D:\\SeleniumNewSW\\msedgedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
title = driver.title
print("Page title: {}".format(title))
assert "Amazon.in" in title
driver.quit()