from time import sleep

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordian = Accordion(browser)
    accordian.visit()
    assert accordian.text_deck.is_visible()
    accordian.drop_click.click()
    sleep(2)
    assert not accordian.text_deck.is_visible()

def test_visible_accordion_default(browser):
    accordian = Accordion(browser)
    accordian.visit()
    assert not accordian.drop_first.is_visible()
    assert not accordian.drop_first_double.is_visible()
    assert not accordian.drop_second.is_visible()