import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.config import Config


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    Config.browser_name = browser
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif  browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()
