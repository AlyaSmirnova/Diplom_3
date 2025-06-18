from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from src.locators import MainPageLocators
from src.locators import LoginPageLocators
from src.locators import PersonalAccountPageLocators
import allure


@allure.feature('Проверка личного кабинета')
class TestPersonalAccountPage:

    def test_personal_account_page_direction_from_main_page(self, driver):
        with allure.step('Проверка перехода в личный кабинет с главной страницы по клику на кнопку "Личный кабинет"'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            assert '/login' in main_page.get_current_url()

    def test_direction_to_history_of_orders(self, driver):
        with allure.step('Проверка перехода в раздел "История заказов" в личном кабинете'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            login_page = LoginPage(driver)
            login_page.wait_for_element(LoginPageLocators.EMAIL)
            login_page.input_text_to_email_field()
            login_page.input_text_to_password_field()
            login_page.click_to_element(LoginPageLocators.LOGIN_BUTTON)
            main_page.wait_for_element(MainPageLocators.MAKE_BURGER_TITLE)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            personal_account_page = PersonalAccountPage(driver)
            WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
            personal_account_page.wait_for_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)
            personal_account_page.click_to_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)
            assert '/account/order-history' in personal_account_page.get_current_url()

