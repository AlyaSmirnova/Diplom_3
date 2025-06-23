from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
import allure


@allure.suite("Восстановления пароля")
class TestResetPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_reset_password_page_direction(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button() # ждем появление кнопки Личный кабинет
        main_page.click_to_personal_account_button() # кликаем на кнопку Личный кабинет

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_visibility_reset_password_button() # ждем появления кнопки Восстановить пароль
        reset_password_page.click_to_reset_password_button() # кликаем на кнопку Восстановить пароль
        assert "/forgot-password" in main_page.get_current_url()


    @allure.title('Проверка ввода email и клика по кнопке "Восстановить"')
    def test_fill_email_input_and_click_reset(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_visibility_reset_password_button()
        reset_password_page.click_to_reset_password_button()
        reset_password_page.wait_for_visibility_email_field() # ждем появления поля ввода для email
        reset_password_page.input_text_to_email_field() # вводим email в поле ввода
        reset_password_page.click_to_new_reset_password_button() # кликаем на кнопку Восстановить
        assert "/reset-password" in reset_password_page.get_current_url()


    @allure.title('Проверка подсветки поля "Пароль" при клике на иконку глаза')
    def test_click_on_eye_button_return_active_field(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_visibility_reset_password_button()
        reset_password_page.click_to_reset_password_button()
        reset_password_page.wait_for_visibility_email_field()
        reset_password_page.input_text_to_email_field()
        reset_password_page.click_to_new_reset_password_button()
        reset_password_page.click_to_eye_icon()
        assert reset_password_page.is_password_field_highlighted()
