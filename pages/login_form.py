from pages.base_page import BasePage
from components.components import WebElements

class RegistrationForm(BasePage):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        super().__init__(driver, self.base_url)

        self.first_name = WebElements(driver, '#firstName')
        self.last_name = WebElements(driver, '#lastName')
        self.user_email  = WebElements(driver, '#userEmail')
        self.dropdown_state = WebElements(driver, '#state > div')
        self.dropdown_city = WebElements(driver, '#city > div')
        self.dropdown_state_choice = WebElements(driver, '#react-select-3-option-3')
        self.dropdown_city_choice = WebElements(driver, '#react-select-4-option-1')
        self.submit = WebElements(driver, '#submit')
        self.form = WebElements(driver, '#userForm')