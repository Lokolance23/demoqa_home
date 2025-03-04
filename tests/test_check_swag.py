from pages.swag_labs import SwagLabs
from conftest import browser

def test_icon(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.icon.exist(browser)

def test_check_name(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.check_username(browser)

def test_check_password(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.check_password(browser)