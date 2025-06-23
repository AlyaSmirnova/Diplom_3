from pages.main_page import MainPage
from src.config import Config
from pages.login_page import LoginPage
import allure


@allure.suite('Проверка основного функционала сайта')
class TestMainFunctionalityPage:

    @allure.title('Проверка перехода на страницу конструктора при клике на кнопку "Конструктор"')
    def test_click_to_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_constructor_button()
        assert main_page.is_constructor_button_highlighted()

    @allure.title('Проверка перехода на страницу Ленты заказов при клике на кнопку "Лента Заказов"')
    def test_click_to_queue_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_orders_queue_button()
        assert "/feed" in main_page.get_current_url()

    @allure.title('Проверка открытия всплывающего окна с детальной информацией при клике на ингредиент')
    def test_click_to_ingredient_open_modal_window_with_info(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_ingredient_bun()
        main_page.wait_for_visibility_open_modal_window()
        assert '/ingredient/61c0c5a71d1f82001bdaaa6d' in main_page.get_current_url()

    @allure.title('Проверка закрытия всплывающего окна ингредиента по клику на иконку крестика')
    def test_click_on_cross_icon_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        main_page.click_to_ingredient_bun()
        main_page.wait_for_visibility_open_modal_window()
        main_page.click_on_cross_icon_for_close_modal_window()
        assert main_page.disappear_of_ingredient_bun_header()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ')
    def test_counter_ingredient_increases_when_added_ingredient(self, driver):
        browser_name = Config.browser_name
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_visibility_of_personal_account_button()
        initial_counter = main_page.get_ingredient_counter() if main_page.get_ingredient_counter() else 0
        main_page.drag_ingredient(browser_name)
        main_page.wait_for_counter_increase()
        final_counter = main_page.get_ingredient_counter()
        assert final_counter == initial_counter + 2

    @allure.title('Проверка, что авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, driver):
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
