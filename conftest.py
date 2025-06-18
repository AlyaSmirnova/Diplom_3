import pytest
from selenium import webdriver
from src.config import Config


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    Config.browser_name = request.param
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

