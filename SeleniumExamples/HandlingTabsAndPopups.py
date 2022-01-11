from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# For Chrome Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://partner.istqb.org/")
driver.maximize_window()
driver.implicitly_wait(5)

windows = driver.window_handles
for window in windows:
    print(window)

driver.find_element_by_xpath("//a[normalize-space()='local Member Board']").click()

# windows = driver.window_handles
# for window in windows:
#     print(window)
#     driver.switch_to.window(window)
#driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//a[@class=' dropdown-toggle'][normalize-space()='Downloads']").click()

# windows = driver.window_handles
# for window in windows:
#     print(window)
#     driver.switch_to.window(window)
#driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//a[normalize-space()='ISTQB CTFL Syllabus 2018 V3.1']").click()


# driver.close()
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# driver.close()

driver.quit()

