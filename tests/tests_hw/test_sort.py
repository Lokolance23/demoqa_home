from time import sleep
from pages.sort import Sort


def test_sort(browser):
    sort = Sort(browser, 'https://demoqa.com/webtables')
    sort.visit()
    sort.btn_sort_salary.click()
    sleep(1)
    assert int(sort.first_salary.get_text()) < int(sort.last_salary.get_text())
    sort.btn_sort_salary.click()
    sleep(1)
    assert int(sort.first_salary.get_text()) > int(sort.last_salary.get_text())
    sort.btn_sort_age.click()
    sleep(1)
    assert int(sort.first_age.get_text()) < int(sort.last_age.get_text())
    sort.btn_sort_age.click()
    sleep(1)
    assert int(sort.first_age.get_text()) > int(sort.last_age.get_text())



