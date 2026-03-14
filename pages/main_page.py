from pages.base_page import BasePage
from src.locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Wait for Personal Account button to be visible')
    def wait_for_visibility_of_personal_account_button(self):
        return self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Click on the Personal Account button')
    def click_to_personal_account_button(self):
        self.click_with_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Wait for modal overlay to disappear before clicking')
    def wait_for_modal_overlay_invisibility(self):
        return self.wait_for_modal_overlay_disappear(MainPageLocators.MODAL_OVERLAY)

    @allure.step('Click on the Constructor button')
    def click_to_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Click on the Order Feed button')
    def click_to_orders_queue_button(self):
        self.click_with_js(MainPageLocators.ORDER_QUEUE_BUTTON)

    @allure.step('Verify that the Constructor button is highlighted')
    def is_constructor_button_highlighted(self):
        container = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return "AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo" in container.get_attribute("class")

    @allure.step('Click on the Fluorescent Bun R2-D3 ingredient')
    def click_to_ingredient_bun(self):
        self.click_to_element(MainPageLocators.INGREDIENT_BUN_BUTTON)

    @allure.step('Wait for ingredient details modal window to appear')
    def wait_for_visibility_open_modal_window(self):
        return self.wait_for_element(MainPageLocators.OPEN_MODAL_WINDOW)

    @allure.step('Click on the close (cross) icon of the modal window')
    def click_on_cross_icon_for_close_modal_window(self):
        self.click_to_element(MainPageLocators.CROSS_ICON_BUTTON)

    @allure.step('Wait for the "Ingredient details" header to disappear')
    def disappear_of_ingredient_bun_header(self):
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_BUN_HEADER)
        return True

    @allure.step('Drag ingredient to the order area using {browser_name} specific method')
    def drag_ingredient(self, browser_name):
        self.wait_of_element_presence(MainPageLocators.INGREDIENT_BUN_BUTTON)
        if browser_name == "chrome":
            self.drag_and_drop_chrome(MainPageLocators.INGREDIENT_BUN_BUTTON, MainPageLocators.ORDER_AREA)
        else:
            self.drag_and_drop_firefox(MainPageLocators.INGREDIENT_BUN_BUTTON, MainPageLocators.ORDER_AREA)

    @allure.step('Get the current value of the ingredient counter')
    def get_ingredient_counter(self):
        counter_element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_element.text)

    @allure.step('Wait for the ingredient counter to increase')
    def wait_for_counter_increase(self):
        self.wait_for_result_of_condition(lambda driver: self.get_ingredient_counter() > 0)

    @allure.step('Click on the "Place Order" button')
    def click_to_create_order_button(self):
        self.wait_for_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_with_js(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Wait for the order ID header to appear')
    def wait_for_id_order_header_appears(self):
        self.wait_for_result_of_condition(
            lambda d: self.wait_for_element(MainPageLocators.ID_ORDER_HEADER).text != "9999"
        )
        return self.wait_for_element(MainPageLocators.ID_ORDER_HEADER)

    @allure.step('Retrieve the order number from the UI')
    def find_order_number_element(self):
        return self.find_element(MainPageLocators.ID_ORDER_HEADER)

    @allure.step('Click on the close (cross) icon for the order confirmation window')
    def click_to_cross_icon_for_close_order(self):
        self.click_with_js(MainPageLocators.CROSS_ICON_BUTTON)

    @allure.step('Wait for user to be authorized (Order button visible)')
    def wait_for_create_order_button(self):
        return self.wait_for_element(MainPageLocators.CREATE_ORDER_BUTTON)
