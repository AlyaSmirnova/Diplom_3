from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
import allure


@allure.feature('Personal Account Functionality')
class TestPersonalAccountPage:

    @allure.story('Navigation')
    @allure.title('Check navigation to Personal Account from Main Page')
    @allure.description('Verify that clicking the "Personal Account" button redirects unauthorized user to the login page.')
    def test_personal_account_page_direction_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()
        assert '/login' in main_page.get_current_url()

    @allure.story('Navigation')
    @allure.title('Check transition to "Order History" section')
    @allure.description('Verify that an authorized user can navigate to the "Order History" section within their account.')
    def test_direction_to_history_of_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_create_order_button()
        main_page.click_to_personal_account_button()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_for_orders_history_button()
        personal_account_page.click_to_orders_history_button()
        assert '/account/order-history' in personal_account_page.get_current_url()

    @allure.story('Authentication')
    @allure.title('Check logout from Personal Account')
    @allure.description('Verify that clicking the "Logout" button correctly terminates the session and redirects to the login page.')
    def test_logout_from_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_create_order_button()
        main_page.click_to_personal_account_button()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_for_logout_button()
        personal_account_page.click_to_logout_button()
        personal_account_page.wait_for_change_url()
        login_page.wait_for_email_field()
        assert "/login" in login_page.get_current_url()
