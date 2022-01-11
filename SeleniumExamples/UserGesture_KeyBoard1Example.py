from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://login.yahoo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#ActionChains(driver).move_to_element(driver.find_element_by_id("identifierId")).perform()
driver.find_element_by_id("login-username").send_keys("boymkeshjunior@yahoo.com")
driver.find_element_by_xpath("//input[@id='login-signin']").send_keys(Keys.ENTER)


