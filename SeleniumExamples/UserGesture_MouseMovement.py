from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()

menu = driver.find_element_by_xpath("//div[contains(text(),'Fashion')]")
action = ActionChains(driver)
action.move_to_element(menu).perform()

driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div/div[4]/a/div[2]/div[2]/div[2]/div/div/div[2]/a[2]").click()