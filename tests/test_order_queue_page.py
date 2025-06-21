from pages.main_page import MainPage
from pages.order_queue_page import OrdersQueuePage
from src.config import Config
from pages.login_page import LoginPage
import allure


@allure.title('Проверка Ленты заказов')
class TestOrderQueuePage:

    def test_click_to_order_modal_window_appears(self, driver):
        with allure.step('Проверка появления всплывающего окна при клике на заказ в Ленте заказов'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            main_page.click_to_orders_queue_button()

            orders_queue_page = OrdersQueuePage(driver)
            orders_queue_page.wait_for_orders_queue_header_appears()
            orders_queue_page.take_first_order_in_orders_queue()
            assert orders_queue_page.find_modal_order_window()

    def test_orders_from_history_are_in_orders_queue(self, driver):
        with allure.step('Проверка, что заказы из "Истории заказов" отображаются в "Ленте заказов"'):
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
            order_number_element = main_page.find_order_number_element()
            order_number = order_number_element.text
            main_page.wait_for_modal_overlay_invisibility()
            main_page.click_to_cross_icon_for_close_order()
            main_page.click_to_orders_queue_button()

            orders_queue_page = OrdersQueuePage(driver)
            orders_queue_page.wait_for_orders_queue_header_appears()
            orders_queue_numbers = orders_queue_page.get_all_orders_numbers()
            assert order_number in orders_queue_numbers

    def test_total_done_count_increases(self, driver):
        with allure.step('Проверка, что при создании нового заказа счетчик Выполнено за все время увеличивается'):
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

    def test_today_orders_increases(self, driver):
        with allure.step('Проверка, что при создании заказа счетчик Выполнено за сегодня увеличивается'):
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

            today_after = orders_queue_page.get_today_orders()
            assert today_after > today_before

    def test_order_number_appears_in_work_section(self, driver):
        with allure.step('Проверка, что после оформления заказа его номер появляется в разделе "В работе"'):
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

            orders_queue_page = OrdersQueuePage(driver)
            orders_queue_page.wait_for_orders_queue_header_appears()
            assert orders_queue_page.is_order_in_progress(order_number)
