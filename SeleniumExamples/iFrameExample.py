from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(5)

# driver.switch_to_frame("iframeResult")
driver.switch_to.frame("iframeResult")
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()

# driver.switch_to_default_content()
driver.switch_to.default_content()
frames = driver.find_elements_by_tag_name("iframe")

for frame in frames:
    print(frame.get_attribute("id"))

print("Total frames are: ", len(frames))