from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import OrdersQueueLocators
from src.locators import MainPageLocators
import allure


class OrdersQueuePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_orders_queue_header_appears(self):
        with allure.step('Дождаться появления заголовка "Лента заказов"'):
            self.wait_for_element(OrdersQueueLocators.ORDERS_QUEUE_HEADER)

    def take_first_order_in_orders_queue(self):
        with allure.step('Взять первый заказ из ленты заказов'):
            self.driver.find_element(*OrdersQueueLocators.FIRST_ORDER_ITEM).click()

    def find_modal_order_window(self):
        with allure.step('Дождаться открытия всплывающего окна с информацией о заказе'):
            return self.driver.find_element(*OrdersQueueLocators.MODAL_FIRST_ORDER_WINDOW)

    def get_all_orders_numbers(self):
        with allure.step('Получить номера всех заказов в Ленте заказов'):
            elements = self.wait_for_elements(OrdersQueueLocators.ORDERS_QUEUE_NUMBERS)
            return [el.text for el in elements]

    def get_total_orders(self):
        with allure.step('Получить значение "Выполнено за всё время"'):
            return int(self.wait_for_elements(OrdersQueueLocators.ORDERS_QUEUE_TOTAL))

    def click_to_personal_account_button(self):
        with allure.step('Кликнуть на копку "Личный кабинет"'):
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(OrdersQueueLocators.PERSONAL_ACCOUNT_BUTTON))
            self.click_to_element(OrdersQueueLocators.PERSONAL_ACCOUNT_BUTTON)

    def get_today_orders(self):
        with allure.step('Получить значение "Выполнено за сегодня"'):
            return int(self.wait_for_elements(OrdersQueueLocators.ORDERS_QUEUE_TODAY))

    def is_order_in_progress(self, order_number):
        with allure.step('Посмотреть, что заказ есть в разделе "В работе"'):
            elements = self.wait_for_elements(OrdersQueueLocators.IN_PROGRESS_ORDERS)
            return any(order_number in el.text for el in elements)