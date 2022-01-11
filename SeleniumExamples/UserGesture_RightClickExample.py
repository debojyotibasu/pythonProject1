import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.maximize_window()
driver.implicitly_wait(5)

img = driver.find_element_by_xpath("//img[@src='data-samples/images/popup_pic.gif']")
ActionChains(driver).context_click(img).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//td[@id='dm2m1i1tdT']")).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//td[@id='dm2m2i1tdT']")).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//td[@id='dm2m3i1tdT']")).perform()
ActionChains(driver).click(driver.find_element_by_xpath("//td[@id='dm2m3i1tdT']")).perform()

time.sleep(3)

driver.quit()