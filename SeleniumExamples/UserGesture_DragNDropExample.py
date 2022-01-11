from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

draggable = driver.find_element_by_id("draggable")
droppable = driver.find_element_by_id("droppable")

ActionChains(driver).drag_and_drop(draggable, droppable).perform()