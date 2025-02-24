import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()