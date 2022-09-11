from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(self.by, self.locator)
        )
        driver.find_element(self.by, self.locator).clear()
        driver.find_element(self.by, self.locator).send_keys(value)
        driver.find_element(self.by, self.locator).send_keys(Keys.RETURN)
        
    
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(self.by, self.locator)
        )
        element = driver.find_element(self.by, self.locator)
        return element.get_attribute("value")