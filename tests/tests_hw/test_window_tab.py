from time import sleep
from pages.win_tab import WinTab


def test_win_tab(browser):
    win = WinTab(browser, 'https://demoqa.com/links')
    win.visit()
    assert win.btn_home.exist()
    assert win.btn_home.get_text() == 'Home'
    assert win.btn_home.get_dom_attr("href") == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    win.btn_home.click()
    assert len(browser.window_handles) == 2




