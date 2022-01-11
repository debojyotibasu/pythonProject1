from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

slider = driver.find_element_by_id("slider")
location = slider.location
size = slider.size
width, height = size['width'], size['height']
print("Location of the main slider is ", location)
print("Size of the main slider is ", size)
print("Width of the main slider is {}".format(width))
print("Height of the main slider is {}".format(height))

sliderHandle = driver.find_element_by_xpath("(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
# ActionChains(driver).drag_and_drop_by_offset(sliderHandle, 300, 0).perform()
ActionChains(driver).drag_and_drop_by_offset(sliderHandle, width/2, 0).perform()
