from time import sleep

from pages.form_page import FormPage

def test_check_text_after_submit(browser):
    form_page = FormPage(browser, 'https://demoqa.com/text-box')
    form_page.visit()
    form_page.full_name.click()
    full_name_example = input("Введите Имя ")
    form_page.full_name.send_keys(full_name_example)
    form_page.current_address.click()
    some_address = input("Введите Адрес ")
    form_page.current_address.send_keys(some_address)
    form_page.submit.click()
    sleep(3)
    assert form_page.full_name_to_compare.get_text() == f'Name:{full_name_example}'
    assert form_page.current_address_to_compare.get_text() == f'Current Address :{some_address}'
