from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

resizableHandle = driver.find_element_by_xpath("//*[@id='resizable']/div[3]")

ActionChains(driver).drag_and_drop_by_offset(resizableHandle,100,-50).perform()