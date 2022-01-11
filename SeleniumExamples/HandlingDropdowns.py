import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver.get("https://echoecho.com/htmlforms11.htm")
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 5)

# driver.find_element_by_name("dropdownmenu").send_keys("Cheese")
# driver.find_element_by_id("searchLanguage").send_keys("Eesti")

dropdown = driver.find_element_by_id("searchLanguage")
select = Select(dropdown)
# select.select_by_visible_text("Eesti")
# select.select_by_value("hi")
select.select_by_index(26)

options = driver.find_elements_by_tag_name("option")
print("Total languages are in list: ", len(options))
for option in options:
    print("Text is: ", option.text + ", Language is: ", option.get_attribute("lang"))

print("====================== PRINTING ALL LINKS ======================")

links = driver.find_elements_by_tag_name("a")
print("Total links are present: ", len(links))
for link in links:
    print("Text is: ", link.text + ", URL is: ", link.get_attribute(("href")))


print("====================== PRINTING ALL LINKS PRESENT IN PARTICULAR SECTION ======================")
block = driver.find_element_by_xpath("//div[@class='other-projects']")
specificLinks = block.find_elements_by_tag_name("a")

print("Total specific links are present: ", len(specificLinks))
for link in specificLinks:
    print("Text is: ", link.text + ", URL is: ", link.get_attribute(("href")))

print("====================== PRINTING ONLY 1ST LINK PRESENT IN PARTICULAR SECTION ======================")
print("1st link text is: ", block.find_elements_by_tag_name("a").__getitem__(0).text)