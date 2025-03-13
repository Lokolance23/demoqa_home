from time import sleep
from pages.modal import ModalPage

def test_open_close(browser):
    modal_dialog = ModalPage(browser, 'https://demoqa.com/modal-dialogs')
    modal_dialog.visit()
    modal_dialog.btn_small_modal.click()
    assert modal_dialog.modal_inf_small.exist()
    modal_dialog.btn_close_small.click()
    sleep(1)
    assert not modal_dialog.modal_inf_small.exist()
    modal_dialog.btn_small_modal.click()
    assert modal_dialog.modal_inf_small.exist()
    modal_dialog.cross_close_small.click()
    sleep(1)
    assert not modal_dialog.modal_inf_small.exist()
    modal_dialog.btn_large_modal.click()
    assert modal_dialog.modal_inf_large.exist()
    modal_dialog.btn_close_large.click()
    sleep(1)
    assert not modal_dialog.modal_inf_large.exist()
    modal_dialog.btn_large_modal.click()
    assert modal_dialog.modal_inf_large.exist()
    modal_dialog.cross_close_large.click()
    sleep(1)
    assert not modal_dialog.modal_inf_large.exist()



