from time import sleep
from pages.alert import Alert


def test_open_close(browser):
    alert = Alert(browser, 'https://demoqa.com/alerts')
    alert.visit()
    alert.btn_alert.click()
    sleep(5)
    assert alert.alert()



