from pages.base_page import BasePage
from src.locators import LoginPageLocators
from src.data import TestData
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Wait for email input field to be visible')
    def wait_for_email_field(self):
        self.wait_for_element(LoginPageLocators.EMAIL)

    @allure.step('Input test email into the Email field')
    def input_text_to_email_field(self):
        self.input_text(LoginPageLocators.EMAIL, TestData.test_email)

    @allure.step('Input test password into the Password field')
    def input_text_to_password_field(self):
        self.input_text(LoginPageLocators.PASSWORD, TestData.test_password)

    @allure.step('Click on the Login button')
    def click_to_button_login(self):
        self.click_with_js(LoginPageLocators.LOGIN_BUTTON)
