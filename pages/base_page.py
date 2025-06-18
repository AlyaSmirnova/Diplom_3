from src.config import Config
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        with allure.step('Открыть главную страницу сайта'):
            self.driver.get(Config.URL)

    def wait_for_element(self, locator, timeout=10):
        with allure.step(f'Дождаться появления элемента {locator}'):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        with allure.step(f'Кликнуть на элемент {locator}'):
            self.wait_for_element(locator).click()

    def get_current_url(self):
        with allure.step("Получить текущий адрес сайта"):
            return self.driver.current_url

    def input_text(self, locator, keys):
        with allure.step(f'Ввести текст{keys} в поле {locator}'):
            self.wait_for_element(locator).send_keys(keys)

#

    #def scroll_to_element(self, locator):
        #with allure.step(f'Проскроллить к элементу {locator}'):
            #element = self.wait_for_element(locator)
            #self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #def get_element_text(self, locator):
        #with allure.step(f'Получить текст элемента {locator}'):
            #element = self.wait_for_element(locator)
            #return element.text



    #def select_dropdown_option(self, dropdown_locator, option_text):
        #with allure.step("Выбрать из выпадающего списка"):
            #self.click_element(dropdown_locator)
            #option_locator = (OrderPageLocators.RENTAL_OPTION[0], OrderPageLocators.RENTAL_OPTION[1].format(option_text))
            #self.click_element(option_locator)

