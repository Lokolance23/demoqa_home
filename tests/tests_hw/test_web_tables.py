from time import sleep

from selenium.webdriver import Keys

from pages.web_table import WebTable

def test_list_of_table(browser):
    list_table = WebTable(browser)
    browser.set_window_size(1800,1800)
    list_table.visit()
    list_table.btn_add.click()
    assert list_table.modal_form.exist()
    list_table.btn_submit.click()
    assert list_table.check_valid.get_dom_attr('class') == 'was-validated'
    list_table.create_note('Petr', 'Ivanov', 'Ivan_p@test.com', '21', '21000', 'MVD')
    sleep(2)
    assert not list_table.modal_form.exist()
    assert list_table.table_last_name.get_text() == 'Ivanov'
    assert list_table.table_first_name.get_text() == 'Petr'
    assert list_table.table_age.get_text() == '21'
    assert list_table.table_email.get_text() == 'Petr@gmail.com'
    assert list_table.table_salary.get_text() == '21000'
    assert list_table.table_department.get_text() == 'MVD'
    list_table.btn_edit.click()
    assert list_table.modal_form.exist()
    list_table.first_name.click()
    list_table.first_name.send_keys(Keys.CONTROL + 'a')
    list_table.first_name.send_keys(Keys.DELETE)
    list_table.first_name.send_keys('Ivan')
    list_table.btn_submit.click()
    sleep(3)
    assert list_table.table_first_name.get_text() == 'Ivan'
    list_table.btn_delete.click()
    assert not list_table.btn_delete.exist()


def test_pagination(browser):
    pag = WebTable(browser)
    browser.set_window_size(1800,1800)
    pag.visit()
    pag.pag_next.click()
    pag.change_rows.scroll_to_element()
    pag.change_rows.click()
    pag.change_rows.send_keys(Keys.UP)
    pag.change_rows.send_keys(Keys.ENTER)
    pag.btn_add.click()
    pag.create_note('Anton', 'Maximov', 'test@tes.kt', '23', '23000', 'MVD')
    sleep(1)
    pag.btn_add.click()
    pag.create_note('Max', 'Pushkin', 'push@mail.com', '43', '50000', 'Sber')
    sleep(1)
    pag.btn_add.click()
    pag.create_note('Vlad', 'Alekseev', 'al@meil.ru', '23', '312000', 'Gazprom')
    pag.pag_next.click()
    assert pag.table_second_first_name.get_text() == 'Vlad'
    sleep(2)
    pag.pag_previous.click()
    assert pag.table_first_name.get_text() == 'Anton'
    sleep(2)
