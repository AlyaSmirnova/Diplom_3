from pages.base_page import BasePage
from src.locators import OrdersQueueLocators
from selenium.common.exceptions import StaleElementReferenceException
import allure


class OrdersQueuePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Wait for the "Order Feed" header to appear')
    def wait_for_orders_queue_header_appears(self):
        self.wait_for_element(OrdersQueueLocators.ORDERS_QUEUE_HEADER)

    @allure.step('Click on the first order in the feed')
    def take_first_order_in_orders_queue(self):
        self.find_element(OrdersQueueLocators.FIRST_ORDER_ITEM).click()

    @allure.step('Wait for the order details modal window to open')
    def find_modal_order_window(self):
        return self.find_element(OrdersQueueLocators.MODAL_FIRST_ORDER_WINDOW)

    @allure.step('Retrieve all order numbers from the Order Feed')
    def get_all_orders_numbers(self):
        for _ in range(3):
            try:
                self.wait_of_element_presence(OrdersQueueLocators.ORDERS_QUEUE_NUMBERS)
                elements = self.driver.find_elements(*OrdersQueueLocators.ORDERS_QUEUE_NUMBERS)
                return [el.text for el in elements if el.text]
            except StaleElementReferenceException:
                continue
        return []

    @allure.step('Get the "Total completed" value')
    def get_total_orders(self):
        element = self.wait_for_element(OrdersQueueLocators.ORDERS_QUEUE_TOTAL)
        return int(element.text)

    @allure.step('Click on the "Personal Account" button')
    def click_to_personal_account_button(self):
        self.click_with_js(OrdersQueueLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Get the "Completed today" value')
    def get_today_orders(self):
        element = self.wait_for_element(OrdersQueueLocators.ORDERS_QUEUE_TODAY)
        return int(element.text)

    @allure.step('Verify if order {order_number} is in the "In progress" section')
    def is_order_in_progress(self, order_number):
        elements = self.wait_for_elements(OrdersQueueLocators.IN_PROGRESS_ORDERS)
        return [el.text for el in elements]

    @allure.step('Wait for specific order {number} to appear in feed')
    def wait_for_order_in_feed(self, number):
        target = number.lstrip('0')
        self.wait_for_result_of_condition(
            lambda d: any(target in n.lstrip('0') for n in self.get_all_orders_numbers())
        )
        return True

    @allure.step('Wait for "Today orders" counter to increase')
    def wait_for_today_counter_to_increase(self, initial_value):
        return self.wait_for_result_of_condition(
            lambda d: self.get_today_orders() > initial_value
        )
