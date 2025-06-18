from pages.base_page import BasePage
from src.locators import ResetPasswordPageLocators
from src.data import TestData
import allure


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_text_to_email_field(self):
        with allure.step('Ввести email в поле "Email"'):
            self.input_text(ResetPasswordPageLocators.EMAIL_FIELD, TestData.test_email)