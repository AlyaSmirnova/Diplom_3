from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    MAKE_BURGER_TITLE = By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"
    MODAL_OVERLAY = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo')]"
    ORDER_QUEUE_BUTTON = By.XPATH, "//p[contains(text(), 'Лента Заказов')]"
    INGREDIENT_BUN_BUTTON = By.XPATH, "//p[contains (text(), 'Флюоресцентная булка R2-D3')]"
    OPEN_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]"
    CROSS_ICON_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]"
    INGREDIENT_BUN_HEADER = By.XPATH, "//h2[text()='Детали ингредиента']"
    ORDER_AREA = By.XPATH, "//div[contains(@class, 'constructor-element constructor-element_pos_top')]"
    INGREDIENT_COUNTER = By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj counter_default__28sqi')]"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    ID_ORDER_HEADER = By.XPATH, "//h2[contains(@class, 'modal__title') or contains(@class, 'OrderDetails_id')]"

class ResetPasswordPageLocators:
    RESET_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"
    EMAIL_FIELD = By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default')]"
    NEW_RESET_PASSWORD_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    EYE_ICON = By.XPATH, "//div[contains(@class, 'input__icon input__icon-action')]"
    HIGHLIGHTED_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input pr-6 pl-6 input_type_text input_size_default input_status_active')]")

class LoginPageLocators:
    EMAIL = By.NAME, "name"
    PASSWORD = By.NAME, "Пароль"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"

class PersonalAccountPageLocators:
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[@href='/account/order-history']"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"

class OrdersQueueLocators:
    ORDERS_QUEUE_HEADER = By.XPATH, "//h1[text()='Лента заказов']"
    FIRST_ORDER_ITEM = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]"
    MODAL_FIRST_ORDER_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10')]"
    ORDERS_QUEUE_NUMBERS = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//p[contains(@class, 'digits-default')]"
    CROSS_ICON_CLOSE_ORDER = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    ORDERS_QUEUE_TOTAL = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    ORDERS_QUEUE_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    IN_PROGRESS_ORDERS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"