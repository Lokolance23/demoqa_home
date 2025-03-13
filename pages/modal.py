from pages.base_page import BasePage
from components.components import WebElements

class ModalPage(BasePage):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        super().__init__(driver, self.base_url)

        self.btn_small_modal = WebElements(driver, '#showSmallModal')
        self.btn_large_modal = WebElements(driver, '#showLargeModal')
        self.modal_inf_small  = WebElements(driver, '#example-modal-sizes-title-sm')
        self.btn_close_small = WebElements(driver, '#closeSmallModal')
        self.cross_close_small = WebElements(driver, 'body > div.fade.modal.show > div > div > div.modal-header > button > span:nth-child(1)')
        self.modal_inf_large = WebElements(driver, '#example-modal-sizes-title-lg')
        self.btn_close_large = WebElements(driver, '#closeLargeModal')
        self.cross_close_large = WebElements(driver, 'body > div.fade.modal.show > div > div > div.modal-header > button > span:nth-child(1)')
