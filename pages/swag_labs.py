from conftest import browser
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElements


class SwagLabs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://www.saucedemo.com/"
        super().__init__(driver, self.base_url)

        self.icon = WebElements(driver, '#root > div > div.login_logo')
        self.user_name = WebElements(driver, '#user-name')
        self.password = WebElements(driver, '#password')


    def check_username(self, browser):
        try:
            self.user_name.find_element()
        except NoSuchElementException:
            return False
        return True

    def check_password(self, browser):
        try:
            self.password.find_element()
        except NoSuchElementException:
            return False
        return True