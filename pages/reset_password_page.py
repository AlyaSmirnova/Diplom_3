from pages.base_page import BasePage
from src.locators import ResetPasswordPageLocators
from src.data import TestData
import allure


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Wait for "Recover Password" button to be visible')
    def wait_for_visibility_reset_password_button(self):
        self.wait_for_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step('Click on the "Recover Password" button')
    def click_to_reset_password_button(self):
        self.click_with_js(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step('Wait for Email input field to appear')
    def wait_for_visibility_email_field(self):
        self.wait_for_element(ResetPasswordPageLocators.EMAIL_FIELD)

    @allure.step('Input test email into the Email field')
    def input_text_to_email_field(self):
        self.input_text(ResetPasswordPageLocators.EMAIL_FIELD, TestData.test_email)

    @allure.step('Click on the "Restore" button and wait for URL change')
    def click_to_new_reset_password_button(self):
        self.click_to_element(ResetPasswordPageLocators.NEW_RESET_PASSWORD_BUTTON)
        self.wait_for_url_contains("/reset-password")

    @allure.step('Click on the Eye icon in the Password field')
    def click_to_eye_icon(self):
        self.wait_for_element_to_be_clickable(ResetPasswordPageLocators.EYE_ICON)
        self.click_to_element(ResetPasswordPageLocators.EYE_ICON)

    @allure.step('Verify if the Password field is highlighted')
    def is_password_field_highlighted(self):
        container = self.find_element(ResetPasswordPageLocators.HIGHLIGHTED_PASSWORD_FIELD)
        return "input_status_active" in container.get_attribute("class")
