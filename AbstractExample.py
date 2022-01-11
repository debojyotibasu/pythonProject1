'''
If a method is without any definition it is called as an Abstract Method
And, the class which is holding that abstract method is called an Abstract Class

By default an Abstract Class/Method creation is not possible in Python, we need some additional modules
need to be added/imported to create Abstract Class/Method
'''
from abc import ABC, abstractmethod

class WebDriver(ABC):

    @abstractmethod
    def click(self):
        pass

class ChromeDriver(WebDriver):
    def captureScreenshot(self):
        print("Capturing Screenshot - Chrome")

    def click(self):
        print("Click on an object - Chrome")



class FirefoxDriver(WebDriver):
    def captureScreenshot(self):
        print("Capturing Screenshot - Firefox")

    def click(self):
        print("Click on an object - Firefox")


# obj1 = WebDriver()
# obj1.click()
obj2 = ChromeDriver()
obj2.captureScreenshot()
obj2.click()
obj3 = FirefoxDriver()
obj3.captureScreenshot()
obj3.click()