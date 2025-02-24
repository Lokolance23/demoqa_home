from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, baseUrl = 'https://www.saucedemo.com/'):
        self.driver = driver
        self.baseUrl = baseUrl

    def visit(self):
        return self.driver.get(self.baseUrl)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)


