from pages.base_page import BasePage
from src.locators import LoginPageLocators
from src.data import TestData
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_email_field(self):
        with allure.step('Дождаться появления поля ввода для email'):
            self.wait_for_element(LoginPageLocators.EMAIL)

    def input_text_to_email_field(self):
        with allure.step('Ввести email в поле "Email"'):
            self.input_text(LoginPageLocators.EMAIL, TestData.test_email)

    def input_text_to_password_field(self):
        with allure.step('Ввести пароль в поле "Пароль"'):
            self.input_text(LoginPageLocators.PASSWORD, TestData.test_password)

    def click_to_button_login(self):
        with allure.step('Кликнуть на кнопку "Войти"'):
            self.click_to_element(LoginPageLocators.LOGIN_BUTTON)