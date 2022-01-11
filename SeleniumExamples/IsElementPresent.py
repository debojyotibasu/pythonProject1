from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Custom made function for checking the presence of the element by it's ID only
# def is_element_present(id):
#     try:
#         driver.find_element_by_id(id)
#         return True
#     except NoSuchElementException:
#         return False

# Custom made function for checking the presence of the element by it's any locator (1st Approach)
def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False

# Custom made function for checking the presence of the element by it's any locator (2nd Approach)
def is_element_present_or_not(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)

# print(driver.find_element_by_id("identifierIddf").is_displayed())
# print(is_element_present("identifierIddf"))

print("====================== USING 1ST APPROACH ======================")
print(is_element_present(By.ID, "identifierId"))
print(is_element_present(By.XPATH, "//*[@id='identifierId123']"))

print("====================== USING 2ND APPROACH ======================")
print(is_element_present_or_not(By.ID, "identifierId123"))
print(is_element_present_or_not(By.XPATH, "//*[@id='identifierId']"))