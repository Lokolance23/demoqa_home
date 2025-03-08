from pages.base_page import BasePage
from components.components import WebElements


class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)
        self.icon = WebElements(driver, '#app > header > a > img')
        self.elements = WebElements(driver,
                                    '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')