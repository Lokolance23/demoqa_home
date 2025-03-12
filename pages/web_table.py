from pages.base_page import BasePage
from components.components import WebElements

class WebTable(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElements(driver, '#addNewRecordButton')
        self.btn_submit = WebElements(driver, '#submit')
        self.first_name = WebElements(driver, '#firstName')
        self.last_name = WebElements(driver, '#lastName')
        self.email = WebElements(driver, '#userEmail')
        self.age = WebElements(driver, '#age')
        self.salary = WebElements(driver, '#salary')
        self.department = WebElements(driver, '#department')

        self.modal_form = WebElements(driver, '#registration-form-modal')
        self.check_valid = WebElements(driver, '#userForm')

        self.table_first_name = WebElements(driver,
                                             '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.table_last_name = WebElements(driver,
                                           '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.table_age = WebElements(driver,
                                     '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.table_email = WebElements(driver,
                                       '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.table_salary = WebElements(driver,
                                        '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.table_department = WebElements(driver,
                                            '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')

        self.btn_edit = WebElements(driver, '#edit-record-4')
        self.btn_delete = WebElements(driver, '#delete-record-4')

        self.pag_next = WebElements(driver, '-next', 'class')
        self.pag_previous = WebElements(driver, '-previous', 'class')
        self.change_rows = WebElements(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')

        self.table_second_first_name = WebElements(driver,
                                             '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')


    def create_note(self, first_name, last_name, email, age, salary, department):
        self.first_name.click()
        self.first_name.send_keys(first_name)
        self.last_name.click()
        self.last_name.send_keys(last_name)
        self.email.click()
        self.email.send_keys(email)
        self.age.click()
        self.age.send_keys(age)
        self.salary.click()
        self.salary.send_keys(salary)
        self.department.click()
        self.department.send_keys(department)
        self.btn_submit.click()