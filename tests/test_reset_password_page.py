from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
import allure


@allure.feature('Password Recovery Functionality')
class TestResetPasswordPage:

    @allure.story('Navigation to Reset Form')
    @allure.title('Check navigation to the "Forgot Password" page')
    @allure.description('Verify that clicking the "Restore Password" link on the Login page redirects to the correct form.')
    def test_reset_password_page_direction(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_visibility_reset_password_button()
        reset_password_page.click_to_reset_password_button()
        assert "/forgot-password" in main_page.get_current_url()

    @allure.story('Password Recovery Process')
    @allure.title('Check email submission for password recovery')
    @allure.description('Verify that entering an email and clicking "Restore" navigates to the final reset step.')
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

    @allure.story('UI Elements')
    @allure.title('Check password field highlighting when clicking the eye icon')
    @allure.description('Verify that clicking the "eye" icon activates the password field and changes its state.')
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
