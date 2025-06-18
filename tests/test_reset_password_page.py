from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from src.locators import MainPageLocators
from src.locators import ResetPasswordPageLocators
import allure


@allure.feature("Восстановления пароля")
class TestResetPasswordPage:

    def test_reset_password_page_direction(self, driver):
        with allure.step('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.wait_for_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            main_page.click_to_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            assert "/forgot-password" in main_page.get_current_url()

    test_email = "alina_smirnova_20@gmail.com"

    def test_fill_email_input_and_click_reset(self, driver):
        with allure.step('Проверка ввода email и клика по кнопке "Восстановить"'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.wait_for_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            main_page.click_to_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            reset_password_page = ResetPasswordPage(driver)
            reset_password_page.wait_for_element(ResetPasswordPageLocators.EMAIL_FIELD)
            reset_password_page.input_text_to_email_field()
            reset_password_page.click_to_element(ResetPasswordPageLocators.NEW_RESET_PASSWORD_BUTTON)
            WebDriverWait(driver, 15).until(EC.url_contains("/reset-password"))
            assert "/reset-password" in reset_password_page.get_current_url()

    def test_click_on_eye_button_return_active_field(self, driver):
        with allure.step('Проверка подсветки поля "Пароль" при клике на иконку глаза'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            main_page.wait_for_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            main_page.click_to_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
            reset_password_page = ResetPasswordPage(driver)
            reset_password_page.wait_for_element(ResetPasswordPageLocators.EMAIL_FIELD)
            reset_password_page.input_text_to_email_field()
            reset_password_page.click_to_element(ResetPasswordPageLocators.NEW_RESET_PASSWORD_BUTTON)
            WebDriverWait(driver, 15).until(EC.url_contains("/reset-password"))
            reset_password_page.click_to_element(ResetPasswordPageLocators.EYE_ICON)
            changed_password_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located(ResetPasswordPageLocators.CHANGED_PASSWORD_FIELD))
            assert "input__placeholder-focused" in changed_password_field.get_attribute("class")

