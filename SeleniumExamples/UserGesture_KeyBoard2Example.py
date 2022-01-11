from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://login.yahoo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# Enter username in username field
driver.find_element_by_id("login-username").send_keys("boymkeshjunior@yahoo.com")

# Click out of the Username input field
driver.find_element_by_xpath("//span[@class='challenge-desc signin-sub-title']").click()

# Select all content of the page using Ctrl + A (Capital 'A' or Small 'a' both will work)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

# Copy all content of the page using Ctrl + C (Capital 'C' or Small 'c' both will work)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

# Return back to Username input box and put cusron at the End of the username text
driver.find_element_by_id("login-username").send_keys(Keys.END)

# Paste all content of the page after the username text using Ctrl + V (Capital 'V' or Small 'v' both will work)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()