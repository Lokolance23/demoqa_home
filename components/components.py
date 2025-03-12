from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class WebElements:
    def __init__(self, driver, locator = "", locator_type = 'css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type


    def get_text(self):
        return str(self.find_element().text)

    def click(self):
        return self.find_element().click()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def is_visible(self):
        return self.find_element().is_displayed()

    def refresh(self):
        self.driver.refresh()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        else:
            return False

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()


    def send_keys(self, text: str):
        self.find_element().send_keys(text)


    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'xpath':
            return By.XPATH

    def get_dom_attr(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);", self.find_element()
        )

    def attr_exist(self, attr):
        if self.driver.getAttribute(attr) is None:
            return False
        else:
            return True