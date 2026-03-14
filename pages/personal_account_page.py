from pages.base_page import BasePage
from src.locators import PersonalAccountPageLocators
from src.locators import MainPageLocators
import allure


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Wait for "Order History" button to appear')
    def wait_for_orders_history_button(self):
        return self.wait_for_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Click on the "Order History" button')
    def click_to_orders_history_button(self):
        self.click_with_js(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Wait for "Personal Account" button to become clickable after authorization')
    def wait_for_personal_account_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Click on the "Personal Account" button')
    def click_to_personal_account_button(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Wait for "Logout" button to appear')
    def wait_for_logout_button(self):
        return self.wait_for_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Click on the "Logout" button')
    def click_to_logout_button(self):
        self.click_to_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Wait for URL to change (Logout process)')
    def wait_for_change_url(self):
        return self.wait_for_url_contains("/login")
