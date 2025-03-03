from pages.demoqa import Demoqa

def test_check_text(browser):
    demoqa = Demoqa(browser)
    demoqa.visit()
    demoqa.text.exist()
    assert demoqa.text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_centr_test(browser):
    demoqa = Demoqa(browser)
    demoqa.visit()
    demoqa.cd.exist()
    demoqa.cd.click()
    demoqa.text_between.exist()
    assert demoqa.text_between.get_text() == 'Please select an item from left to start practice.'




