from pages.base_page import BasePage
from src.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_visibility_of_personal_account_button(self):
        with allure.step('Дождаться видимости кнопки "Личный кабинет"'):
            self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_to_personal_account_button(self):
        with allure.step('Кликнуть на кнопку "Личный кабинет"'):
            self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def wait_for_modal_overlay_invisibility(self):
        with allure.step('Дождаться исчезновения модального окна для клика на кнопку "Личный кабинет"'):
            self.wait_for_modal_overlay_disappear(MainPageLocators.MODAL_OVERLAY)

    def click_to_constructor_button(self):
        with allure.step('Кликнуть на кнопку "Конструктор"'):
            self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_to_orders_queue_button(self):
        with allure.step('Кликнуть на кнопку "Лента Заказов"'):
            self.click_to_element(MainPageLocators.ORDER_QUEUE_BUTTON)

    def is_constructor_button_highlighted(self):
        with allure.step('Получить подтверждение, что кнопка "Конструктор" подсвечена'):
            container = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
            return "AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo" in container.get_attribute("class")

    def click_to_ingredient_bun(self):
        with allure.step('Кликнуть на ингредиент "Флюоресцентная булка R2-D3"'):
            self.click_to_element(MainPageLocators.INGREDIENT_BUN_BUTTON)

    def wait_for_visibility_open_modal_window(self):
        with allure.step('Дождаться появления всплывающего окна с информацией о выбранном ингредиенте'):
            self.wait_for_element(MainPageLocators.OPEN_MODAL_WINDOW)

    def click_on_cross_icon_for_close_modal_window(self):
        with allure.step('Кликнуть на иконку крестика всплывающего окна с информацией об ингредиенте'):
            self.click_to_element(MainPageLocators.CROSS_ICON_BUTTON)

    def disappear_of_ingredient_bun_header(self):
        with allure.step('Дождаться исчезновения заголовка "Детали ингредиента"'):
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_BUN_HEADER))
            return True

    def drag_ingredient(self, browser_name):
        with allure.step('Использовать подходящий для браузера метод drag_and_drop'):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.INGREDIENT_BUN_BUTTON))
            if browser_name == "chrome":
                self.drag_and_drop_chrome(MainPageLocators.INGREDIENT_BUN_BUTTON, MainPageLocators.ORDER_AREA)
            else:
                self.drag_and_drop_firefox(MainPageLocators.INGREDIENT_BUN_BUTTON, MainPageLocators.ORDER_AREA)

    def get_ingredient_counter(self):
        with allure.step('Получить число, на которое увеличился счетчик ингрелдинетов'):
            counter_element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
            return int(counter_element.text)

    def wait_for_counter_increase(self):
        with allure.step('Дождаться увеличения счетчика'):
            WebDriverWait(self.driver, 15).until(lambda driver: self.get_ingredient_counter() > 0)

    def click_to_create_order_button(self):
        with allure.step('Кликнуть на кнопку "Оформить заказ"'):
            self.wait_for_element(MainPageLocators.CREATE_ORDER_BUTTON)
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MainPageLocators.CREATE_ORDER_BUTTON)).click()

    def wait_for_id_order_header_appears(self):
        with allure.step('Дождаться появления заголовка "идентификатор заказа"'):
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.ID_ORDER_HEADER))
            return True

    def find_order_number_element(self):
        with allure.step('Найти номер заказа пользователя'):
            return self.driver.find_element(*MainPageLocators.ID_ORDER_HEADER)

    def click_to_cross_icon_for_close_order(self):
        with allure.step('Кликнуть на иконку закрытия окна оформления заказа'):
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.CROSS_ICON_BUTTON))
            self.click_to_element(MainPageLocators.CROSS_ICON_BUTTON)

