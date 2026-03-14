from pages.main_page import MainPage
from pages.order_queue_page import OrdersQueuePage
from src.config import Config
from pages.login_page import LoginPage
import allure


@allure.feature('Order Feed Functionality')
class TestOrderQueuePage:

    @allure.story('Order Details Modal')
    @allure.title('Check order details modal opens in Order Feed')
    @allure.description('Verify that clicking on an order card opens a modal window with details.')
    def test_click_to_order_modal_window_appears(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_orders_queue_button()

        orders_queue_page = OrdersQueuePage(driver)
        orders_queue_page.wait_for_orders_queue_header_appears()
        orders_queue_page.take_first_order_in_orders_queue()
        assert orders_queue_page.find_modal_order_window()

    @allure.story('Order Synchronization')
    @allure.title('Check that user orders appear in Order Feed')
    @allure.description('Verify that a newly created order ID is visible in the general Order Feed list.')
    def test_orders_from_history_are_in_orders_queue(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_visibility_of_personal_account_button()
        main_page.drag_ingredient(Config.browser_name)
        main_page.wait_for_counter_increase()
        main_page.click_to_create_order_button()
        main_page.wait_for_id_order_header_appears()
        order_number_element = main_page.wait_for_id_order_header_appears()
        order_number = order_number_element.text
        main_page.click_to_cross_icon_for_close_order()
        main_page.wait_for_modal_overlay_invisibility()
        main_page.click_to_orders_queue_button()

        orders_queue_page = OrdersQueuePage(driver)
        orders_queue_page.wait_for_orders_queue_header_appears()
        orders_queue_page.get_all_orders_numbers()
        assert orders_queue_page.wait_for_order_in_feed(order_number)

    @allure.story('Order Statistics')
    @allure.title('Total orders counter increases after new order')
    def test_total_done_count_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        orders_queue_page = OrdersQueuePage(driver)
        main_page.click_to_orders_queue_button()
        orders_queue_page.wait_for_orders_queue_header_appears()
        total_before = orders_queue_page.get_total_orders()
        orders_queue_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_visibility_of_personal_account_button()
        main_page.drag_ingredient(Config.browser_name)
        main_page.wait_for_counter_increase()
        main_page.click_to_create_order_button()
        main_page.wait_for_id_order_header_appears()
        main_page.click_to_orders_queue_button()

        total_after = orders_queue_page.get_total_orders()
        assert total_after > total_before

    @allure.story('Order Statistics')
    @allure.title('Today orders counter increases after new order')
    def test_today_orders_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        orders_queue_page = OrdersQueuePage(driver)
        main_page.click_to_orders_queue_button()
        orders_queue_page.wait_for_orders_queue_header_appears()
        today_before = orders_queue_page.get_today_orders()
        orders_queue_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_visibility_of_personal_account_button()
        main_page.drag_ingredient(Config.browser_name)
        main_page.wait_for_counter_increase()
        main_page.click_to_create_order_button()
        main_page.wait_for_id_order_header_appears()
        main_page.click_to_orders_queue_button()

        orders_queue_page.wait_for_today_counter_to_increase(today_before)
        today_after = orders_queue_page.get_today_orders()
        assert today_after > today_before

    @allure.story('Order Status')
    @allure.title('Order number appears in "In Progress" section')
    @allure.description('Verify that after placing an order, its ID is displayed in the "Work" section of the feed.')
    def test_order_number_appears_in_work_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_personal_account_button()

        login_page = LoginPage(driver)
        login_page.wait_for_email_field()
        login_page.input_text_to_email_field()
        login_page.input_text_to_password_field()
        login_page.click_to_button_login()

        main_page.wait_for_visibility_of_personal_account_button()
        main_page.drag_ingredient(Config.browser_name)
        main_page.wait_for_counter_increase()
        main_page.click_to_create_order_button()
        order_number_element = main_page.wait_for_id_order_header_appears()
        order_number = order_number_element.text

        main_page.click_to_cross_icon_for_close_order()
        main_page.wait_for_modal_overlay_invisibility()
        main_page.click_to_orders_queue_button()

        orders_queue_page = OrdersQueuePage(driver)
        orders_queue_page.wait_for_orders_queue_header_appears()
        assert orders_queue_page.is_order_in_progress(order_number)
