from selenium.webdriver import ActionChains
from src.config import Config
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        with allure.step('Открыть главную страницу сайта'):
            self.driver.get(Config.URL)

    def find_element(self, locator):
        with allure.step(f'Найти элемент {locator}'):
            by, value = locator # распаковка кортежа
            return self.driver.find_element(by, value)

    def wait_for_element(self, locator, timeout=10):
        with allure.step(f'Дождаться появления элемента {locator}'):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        with allure.step(f'Кликнуть на элемент {locator}'):
            self.wait_for_element(locator).click()

    def get_current_url(self):
        with allure.step("Получить текущий адрес сайта"):
            return self.driver.current_url

    def input_text(self, locator, keys):
        with allure.step(f'Ввести текст{keys} в поле {locator}'):
            self.wait_for_element(locator).send_keys(keys)

    def wait_for_modal_overlay_disappear(self, locator):
        with allure.step('Дождаться, когда исчезнет перекрывающее модальное окно'):
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_chrome(self, locator_from, locator_to): # метод действует только для Chrome
        with allure.step('Перетащить ингредиент в заказ для браузера Chrome'):
            elem_from = self.find_element(locator_from)
            elem_to = self.find_element(locator_to)
            ActionChains(self.driver).drag_and_drop(elem_from, elem_to).perform()

    def drag_and_drop_firefox(self, locator_from, locator_to):
        with allure.step('Перетащить ингредиент в заказ для браузера Firefox'):
            elem_from = self.find_element(locator_from)
            elem_to = self.find_element(locator_to)
            self.driver.execute_script("""
                        function createEvent(typeOfEvent) {
                            var event = document.createEvent("CustomEvent");
                            event.initCustomEvent(typeOfEvent, true, true, null);
                            event.dataTransfer = {
                                data: {},
                                setData: function(key, value) {
                                    this.data[key] = value;
                                },
                                getData: function(key) {
                                    return this.data[key];
                                }
                            };
                            return event;
                        }

                        function dispatchEvent(element, event, transferData) {
                            if (transferData !== undefined) {
                                event.dataTransfer = transferData;
                            }
                            element.dispatchEvent(event);
                        }

                        var source = arguments[0];
                        var target = arguments[1];

                        var dragStartEvent = createEvent('dragstart');
                        dispatchEvent(source, dragStartEvent);

                        var dropEvent = createEvent('drop');
                        dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);

                        var dragEndEvent = createEvent('dragend');
                        dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
                    """, elem_from, elem_to)

    def wait_for_elements(self, locator):
        with allure.step('Найти элементы'):
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located(locator))
