from selenium.webdriver.common.by import By

# локаторы главной страницы
class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    MAKE_BURGER_TITLE = By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"

# локаторы страницы восстановления пароля
class ResetPasswordPageLocators:
    RESET_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"
    EMAIL_FIELD = By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default')]"
    NEW_RESET_PASSWORD_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    EYE_ICON = By.XPATH, "//div[contains(@class, 'input__icon input__icon-action')]"
    CHANGED_PASSWORD_FIELD = By.XPATH, "//label[contains(@class, 'input__placeholder text noselect text_type_main-default input__placeholder-focused')]"

# локаторы для страницы входа:
class LoginPageLocators:
    EMAIL = By.NAME, "name"
    PASSWORD = By.NAME, "Пароль"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"

# локаторы личного кабинета
class PersonalAccountPageLocators:
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[contains(text(), 'История заказов')]"

