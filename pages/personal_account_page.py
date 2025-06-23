from pages.base_page import BasePage
from src.locators import PersonalAccountPageLocators
from src.locators import MainPageLocators
import allure


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_orders_history_button(self):
        with allure.step('Дождаться появления кнопки "История заказов"'):
            self.wait_for_url_contains("/account/profile")
            self.wait_for_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    def click_to_orders_history_button(self):
        with allure.step('Клинкуть на кнопку "История заказов"'):
            self.click_to_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    def wait_for_personal_account_button_is_clickable(self):
        with allure.step('Дождаться кликабельности кнопки "личный кабинет" после авторизации'):
            self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_to_personal_account_button(self):
        with allure.step('Кликнуть на кнопку "Личный кабинет"'):
            self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def wait_for_logout_button(self):
        with allure.step('Дождаться появления кнопки "Выход"'):
            self.wait_for_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    def click_to_logout_button(self):
        with allure.step('Кликнуть по кнопке "Выход"'):
            self.click_to_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    def wait_for_change_url(self):
        with allure.step('Дождаться изменения URL'):
            self.wait_for_url_contains("/login")
