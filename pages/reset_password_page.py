from pages.base_page import BasePage
from src.locators import ResetPasswordPageLocators
from src.data import TestData
import allure


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_visibility_reset_password_button(self):
        with allure.step('Дождаться видимости кнопки "Восстановить пароль"'):
            self.wait_for_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def click_to_reset_password_button(self):
        with allure.step('Кликнуть на кнопку "Восстановить пароль"'):
            self.click_to_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def wait_for_visibility_email_field(self):
        with allure.step('Дождаться появления поля ввода для email'):
            self.wait_for_element(ResetPasswordPageLocators.EMAIL_FIELD)

    def input_text_to_email_field(self):
        with allure.step('Ввести email в поле "Email"'):
            self.input_text(ResetPasswordPageLocators.EMAIL_FIELD, TestData.test_email)

    def click_to_new_reset_password_button(self):
        with allure.step('Кликнуть на кнопку "Восстановить"'):
            self.click_to_element(ResetPasswordPageLocators.NEW_RESET_PASSWORD_BUTTON)
            self.wait_for_url_contains("/reset-password")

    def click_to_eye_icon(self):
        with allure.step('Кликнуть на иконку глаза в поле Пароль'):
            self.wait_for_element_to_be_clickable(ResetPasswordPageLocators.EYE_ICON)
            self.click_to_element(ResetPasswordPageLocators.EYE_ICON)

    def is_password_field_highlighted(self):
        with allure.step('Получить подтверждение, что поле "Пароль" подсвечено'):
            container = self.find_element(ResetPasswordPageLocators.HIGHLIGHTED_PASSWORD_FIELD)
            return "input_status_active" in container.get_attribute("class")
