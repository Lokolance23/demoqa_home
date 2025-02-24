from conftest import browser
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):

    def exist_icon(self, browser):

        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def check_username(self, browser):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def check_password(self, browser):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True