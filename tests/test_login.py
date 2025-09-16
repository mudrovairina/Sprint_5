from auth_helpers import login
from locators import LoginLocators, CommonAuthLocators
from urls import BASE_URL, REGISTER_URL, PASSWORD_RECOVERY_URL, LOGIN_URL


class TestLogin:
    def test_login_main_page_button(self, driver, registered_user):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(BASE_URL)
        driver.find_element(*LoginLocators.BUTTON_LOGIN_MAIN).click()
        login(
            driver,
            registered_user,
            wait_for_element=LoginLocators.BUTTON_ORDER
        )
        assert driver.current_url == BASE_URL

    def test_login_personal_account_button(self, driver, registered_user):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(BASE_URL)
        driver.find_element(*LoginLocators.LOGIN_ACCOUNT).click()
        login(
            driver,
            registered_user,
            wait_for_element=LoginLocators.BUTTON_ORDER
        )
        assert driver.current_url == BASE_URL

    def test_login_registration_form_button(self, driver, registered_user):
        """Вход через кнопку в форме регистрации"""
        driver.get(REGISTER_URL)
        driver.find_element(*LoginLocators.LOGIN_LINK).click()
        login(
            driver,
            registered_user,
            wait_for_element=LoginLocators.BUTTON_ORDER
        )
        assert driver.current_url == BASE_URL

    def test_login_password_recovery_form_button(self, driver, registered_user):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(PASSWORD_RECOVERY_URL)
        driver.find_element(*LoginLocators.LOGIN_LINK).click()
        login(
            driver,
            registered_user,
            wait_for_element=LoginLocators.BUTTON_ORDER
        )
        assert driver.current_url == BASE_URL

    def test_login_invalid_email(self, driver, registered_user):
        """Неверный email — остаемся на странице логина"""
        driver.get(LOGIN_URL)
        wrong_user = registered_user.copy()
        wrong_user["email"] = "wrongemail@example.com"
        login(
            driver,
            wrong_user,
            wait_for_element=CommonAuthLocators.HEADER_LOGIN
        )
        assert driver.current_url == LOGIN_URL

    def test_login_invalid_password(self, driver, registered_user):
        """Неверный пароль — остаемся на странице логина"""
        driver.get(LOGIN_URL)
        wrong_user = registered_user.copy()
        wrong_user["password"] = "wrongpass"
        login(
            driver,
            wrong_user,
            wait_for_element=CommonAuthLocators.HEADER_LOGIN
        )
        assert driver.current_url == LOGIN_URL
