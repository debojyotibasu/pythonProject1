import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# For Firefox Browser
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# Capture Page Screenshot Function
def capture_pagescreenshot(drv, path):
    pagescrfilename = path + "pageScreenshot_" + time.asctime().replace(":", "_") + ".png"
    drv.save_screenshot(pagescrfilename)


# # Capture Element Screenshot Function
# def capture_elementscreenshot(elem, path):
#     elemscrfilename = path + "elementScreenshot_" + time.asctime().replace(":", "_") + ".jpg"
#     elem.screenshot(elemscrfilename)


driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(5)

# driver.save_screenshot("./screenshot/error.png")

driver.switch_to.frame("iframeResult")
driver.execute_script("myFunction()")

elmnt = driver.find_element_by_id("mySubmit")
elmnt.screenshot("./screenshot/element.jpg")
driver.execute_script("arguments[0].style.border='3px solid red'", elmnt)

driver.switch_to.default_content()

capture_pagescreenshot(driver, "./screenshot/")
# capture_elementscreenshot(elmnt, "./screenshot/")
