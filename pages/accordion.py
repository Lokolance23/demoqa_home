from pages.base_page import BasePage
from components.components import WebElements


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)
        self.text_deck = WebElements(driver, '#section1Content > p')
        self.drop_click = WebElements(driver, '#section1Heading')
        self.drop_first = WebElements(driver, '#section2Content > p:nth-child(1)')
        self.drop_first_double = WebElements(driver, '#section2Content > p:nth-child(2)')
        self.drop_second = WebElements(driver, '#section3Content > p')



