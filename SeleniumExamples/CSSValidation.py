from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/css/default.asp")
driver.maximize_window()
driver.implicitly_wait(1)

print(driver.find_element_by_xpath("//a[@class='active']").value_of_css_property("font-family"))
print(driver.find_element_by_xpath("//a[@class='active']").value_of_css_property("padding"))
print(driver.find_element_by_xpath("//a[@class='active']").value_of_css_property("font-size"))
print(driver.find_element_by_xpath("//a[@class='active']").value_of_css_property("background-color"))

driver.quit()