import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@title='Sign in']").click()

# alert = driver.switch_to_alert()
alert = Alert(driver)
print(alert.text)
time.sleep(3)
alert.accept()

driver.quit()