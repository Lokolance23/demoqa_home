from pages.modal_dialogs import ModalDialog

def test_modal_elements(browser):
    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()
    assert modal_dialog.elements.check_count_elements(count = 5)

def test_navigation_modal(browser):
    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()
    browser.refresh()
    modal_dialog.icon.click()
    browser.back()
    browser.set_window_size(900, 600)
    browser.forward()
    assert modal_dialog.equal_url()
    assert browser.title == "DEMOQA"
    browser.set_window_size(1000, 1000)



