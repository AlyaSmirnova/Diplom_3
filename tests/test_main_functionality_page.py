from pages.main_page import MainPage
from src.config import Config
from pages.login_page import LoginPage
import allure


@allure.title('Проверка основного функционала сайта')
class TestMainFunctionalityPage:

    def test_click_to_constructor_button(self, driver):
        with allure.step('Проверка перехода на страницу конструктора при клике на кнопку "Конструктор"'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            main_page.click_to_constructor_button()
            assert main_page.is_constructor_button_highlighted()

    def test_click_to_queue_button(self, driver):
        with allure.step('Проверка перехода на страницу Ленты заказов при клике на кнопку "Лента Заказов"'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            main_page.click_to_orders_queue_button()
            assert "/feed" in main_page.get_current_url()

    def test_click_to_ingredient_open_modal_window_with_info(self, driver):
        with allure.step('Проверка открытия всплывающего окна с детальной информацией при клике на ингредиент'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            main_page.click_to_ingredient_bun()
            main_page.wait_for_visibility_open_modal_window()
            assert '/ingredient/61c0c5a71d1f82001bdaaa6d' in main_page.get_current_url()

    def test_click_on_cross_icon_close_modal_window(self, driver):
        with allure.step('Проверка закрытия всплывающего окна ингредиента по клику на иконку крестика'):
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            main_page.click_to_ingredient_bun()
            main_page.wait_for_visibility_open_modal_window()
            main_page.click_on_cross_icon_for_close_modal_window()
            assert main_page.disappear_of_ingredient_bun_header()

    def test_counter_ingredient_increases_when_added_ingredient(self, driver):
        with allure.step('Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ'):
            browser_name = Config.browser_name
            main_page = MainPage(driver)
            main_page.open_page()
            main_page.wait_for_visibility_of_personal_account_button()
            initial_counter = main_page.get_ingredient_counter() if main_page.get_ingredient_counter() else 0
            main_page.drag_ingredient(browser_name)
            main_page.wait_for_counter_increase()
            final_counter = main_page.get_ingredient_counter()
            assert final_counter == initial_counter + 2

    def test_authorized_user_can_create_order(self, driver):
        with allure.step('Проверка, что авторизованный пользователь может оформить заказ'):
            browser_name = Config.browser_name
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
            main_page.drag_ingredient(browser_name)
            main_page.wait_for_counter_increase()
            main_page.click_to_create_order_button()
            assert main_page.wait_for_id_order_header_appears()
