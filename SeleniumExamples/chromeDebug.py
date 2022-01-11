from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# driver.maximize_window()
# driver.implicitly_wait(1)
# driver.find_element_by_id("identifierId").send_keys("aritra.sanjoy.rajat")





