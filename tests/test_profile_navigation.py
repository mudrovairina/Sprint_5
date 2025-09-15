from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helpers import login
from locators import LoginLocators, ProfileNavigationLocators
from urls import BASE_URL, PROFILE_URL, LOGIN_URL


class TestProfileNavigation:
    def test_go_to_personal_account_registered_user(
            self,
            driver,
            registered_user
    ):
        """Переход зарегистрированного пользователя в личный кабинет"""
        login(driver, registered_user)
        driver.find_element(*LoginLocators.LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(PROFILE_URL))
        assert driver.current_url == PROFILE_URL

    def test_go_from_personal_account_to_constructor(
            self,
            driver,
            registered_user
    ):
        """
        Переход из личного кабинета в конструктор по кнопке
        'Конструктор'
        """
        login(driver, registered_user)
        driver.find_element(*LoginLocators.LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                ProfileNavigationLocators.BUTTON_CONSTRUCTOR
            )
        ).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_go_from_personal_account_to_stellar_burgers_logo(
            self,
            driver,
            registered_user
    ):
        """
        Переход из личного кабинета в конструктор по клику на логотип
        """
        login(driver, registered_user)
        driver.find_element(*LoginLocators.LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                ProfileNavigationLocators.STELLAR_BURGERS_LOGO
            )
        ).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_logout_from_personal_account_redirects_to_login_page(
            self,
            driver,
            registered_user
    ):
        """Выход из личного кабинета и редирект на страницу логина"""
        login(driver, registered_user)
        driver.find_element(*LoginLocators.LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                ProfileNavigationLocators.BUTTON_LOGOUT
            )
        ).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
