import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# For Chrome Browser
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# For Firefox Browser
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)

# username = driver.find_element_by_id("identifierId")
# username.send_keys("djbasu2010@gmail.com")

driver.find_element_by_id("identifierId").send_keys("boymkeshjunior@gmail.com")
driver.find_element_by_xpath("//span[normalize-space()='Next']").click()

# time.sleep(2)
# //*[@id='password']/div[1]/div//div[1]/input
element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div//div[1]/input")))

#driver.find_element_by_xpath("//*[@id='password']/div[1]/div//div[1]/input").send_keys("pass@123456")
element.send_keys("pass@123456")

button = driver.find_element_by_xpath\
    ("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']//div[@class='VfPpkd-RLmnJb']")
driver.execute_script("arguments[0].click();", button)

errorMsg = driver.find_element_by_xpath(
    "//span[contains(text(),'Wrong password. Try again or click ‘Forgot passwor')]"
).text
print(errorMsg)