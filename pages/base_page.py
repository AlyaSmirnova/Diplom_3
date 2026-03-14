from selenium.webdriver import ActionChains
from src.config import Config
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        with allure.step(f'Open main page: {Config.URL}'):
            self.driver.get(Config.URL)

    def wait_for_element_to_disappear(self, locator):
        with allure.step(f'Wait for element {locator} to disappear'):
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def find_element(self, locator):
        with allure.step(f'Find element by locator: {locator}'):
            by, value = locator
            return self.driver.find_element(by, value)

    def wait_for_element(self, locator, timeout=10):
        with allure.step(f'Wait for element {locator} to be visible'):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        with allure.step(f'Click on element: {locator}'):
            self.wait_for_element(locator).click()

    def get_current_url(self):
        with allure.step("Get current browser URL"):
            return self.driver.current_url

    def input_text(self, locator, keys):
        with allure.step(f'Input text into {locator}'):
            self.wait_for_element(locator).send_keys(keys)

    def wait_for_modal_overlay_disappear(self, locator):
        with allure.step('Wait for modal overlay/popup to disappear'):
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_chrome(self, locator_from, locator_to): # only for Chrome
        with allure.step('Perform Drag-and-Drop for Chrome browser'):
            elem_from = self.find_element(locator_from)
            elem_to = self.find_element(locator_to)
            ActionChains(self.driver).drag_and_drop(elem_from, elem_to).perform()

    def drag_and_drop_firefox(self, locator_from, locator_to):
        with allure.step('Perform Drag-and-Drop for Firefox browser via JS script'):
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
        with allure.step(f'Wait for all elements located by {locator}'):
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located(locator))

    def wait_of_element_presence(self, locator):
        with allure.step(f'Wait for presence of element {locator} in DOM'):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_for_result_of_condition(self, condition_function):
        with allure.step('Wait for custom expected condition result'):
            WebDriverWait(self.driver, 15).until(condition_function)

    def wait_for_element_to_be_clickable(self, locator):
        with allure.step(f'Wait for element {locator} to become clickable'):
            return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, text):
        with allure.step(f'Wait for browser URL to contain: "{text}"'):
            WebDriverWait(self.driver, 15).until(EC.url_contains(text))

    @allure.step('Force click on element using JavaScript: {locator}')
    def click_with_js(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
