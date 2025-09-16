from selenium.webdriver.common.by import By


class CommonAuthLocators:
    """Общие локаторы для форм входа и регистрации"""
    INPUT_EMAIL = (
        By.XPATH,
        ".//label[text()='Email']/following-sibling::input"
    )
    INPUT_PASSWORD = (
        By.XPATH,
        ".//label[text()='Пароль']/following-sibling::input"
    )
    HEADER_LOGIN = (By.XPATH, "//h2[text()='Вход']")

class RegistrationLocators:
    """Локаторы формы регистрации"""
    INPUT_NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    BUTTON_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    INVALID_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")
    HEADER_REGISTRATION = (By.XPATH, "//h2[text()='Регистрация']")
    EXISTING_EMAIL_ERROR = (
        By.XPATH,
        "//p[text()='Такой пользователь уже существует']"
    )

class LoginLocators:
    """Локаторы формы входа"""
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']")
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")

class ProfileNavigationLocators:
    """Локаторы элементов навигации внутри личного кабинета пользователя"""
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, 'a[href="/"]')
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")

class ConstructorTabsLocators:
    """Локаторы разделов конструктора: Булки, Соусы, Начинки"""
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
