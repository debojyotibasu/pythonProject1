from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.implicitly_wait(1)

# driver.save_screenshot("./screenshot/errFullPageSCR.jpg")
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S("Width"), S("Height"))

driver.find_element_by_tag_name("body").screenshot('./screenshot/fullPage.png')