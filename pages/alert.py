from pages.base_page import BasePage
from components.components import WebElements

class Alert(BasePage):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElements(driver, '#timerAlertButton')

