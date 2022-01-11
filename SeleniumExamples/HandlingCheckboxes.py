from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Custom made function for checking the presence of the element by it's any locator
def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
driver.implicitly_wait(10)

# Check all checkboxes one-by-one
# driver.find_element_by_xpath("//div[4]//input[1]").click()
# driver.find_element_by_xpath("//div[4]//input[2]").click()
# driver.find_element_by_xpath("//div[4]//input[3]").click()
# driver.find_element_by_xpath("//div[4]//input[4]").click()

# Check all checkboxes one-by-one but using a logic (1st approach)
# i = 1
# while is_element_present(By.XPATH, "//div[4]//input[" + str(i) + "]"):
#     driver.find_element_by_xpath("//div[4]//input[" + str(i) + "]").click()
#     i += 1
# print("Total checkboxes are: ", i - 1)

# # Check all checkboxes one-by-one but using a logic (2nd approach)
# checkboxes = driver.find_elements(By.NAME, "sports")
#
# print("Total checkboxes in a block: ", len(checkboxes))
# for checkbox in checkboxes:
#     print("Before clicking: ", checkbox.is_selected())
#     checkbox.click()
#     print("After clicking: ", checkbox.is_selected())

# # Check all checkboxes one-by-one but using a logic (2nd upgraded approach where we use first block of the page)
block = driver.find_element_by_xpath("//tbody//tr//div[4]")
checkboxes = block.find_elements(By.NAME, "sports")

print("Total checkboxes in a block: ", len(checkboxes))
for checkbox in checkboxes:
    print("Before clicking: ", checkbox.is_selected())
    checkbox.click()
    print("After clicking: ", checkbox.is_selected())