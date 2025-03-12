from time import sleep

from pages.login_form import RegistrationForm

def test_check_validate(browser):
    reg_page = RegistrationForm(browser, 'https://demoqa.com/automation-practice-form')
    reg_page.visit()
    assert reg_page.first_name.get_dom_attr(name = 'placeholder') == 'First Name'
    assert reg_page.last_name.get_dom_attr(name = 'placeholder') == 'Last Name'
    assert reg_page.user_email.get_dom_attr(name = 'placeholder') == 'name@example.com'
    assert reg_page.user_email.get_dom_attr(name = 'pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

def test_submit_empty_forms(browser):
    reg_page = RegistrationForm(browser,'https://demoqa.com/automation-practice-form')
    reg_page.visit()
    reg_page.submit.scroll_to_element()
    reg_page.submit.click()
    assert reg_page.form.get_dom_attr('class') == 'was-validated'

def test_input_state_city(browser):
    login_form = RegistrationForm(browser, 'https://demoqa.com/automation-practice-form')
    login_form.visit()
    login_form.dropdown_state.scroll_to_element()
    login_form.dropdown_state.click()
    login_form.dropdown_state_choice.click()
    login_form.dropdown_city.click()
    login_form.dropdown_city_choice.click()
