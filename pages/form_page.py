from pages.base_page import BasePage
from components.components import WebElements

class FormPage(BasePage):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        super().__init__(driver, self.base_url)

        self.full_name = WebElements(driver, '#userName')
        self.current_address = WebElements(driver, '#currentAddress')
        self.full_name_to_compare = WebElements(driver, '#name')
        self.current_address_to_compare = WebElements(driver, 'p#currentAddress')
        self.submit = WebElements(driver, "#submit")
