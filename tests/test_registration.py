from auth_helpers import register_user_ui
from locators import CommonAuthLocators, RegistrationLocators
from urls import REGISTER_URL
from user_generator import registration_user


class TestRegistration:
    def test_registration_valid_name_email_password_success(self, driver):
        """Регистрация: валидные имя, email и пароль"""
        user = registration_user()
        # Ждем перехода на страницу логина после успешной регистрации
        register_user_ui(
            driver,
            user,
            wait_for_element=CommonAuthLocators.HEADER_LOGIN
        )
        assert "/login" in driver.current_url

    def test_registration_invalid_password_error(self, driver):
        """Некорректный пароль '123' — появляется сообщение об ошибке"""
        user = registration_user()
        user["password"] = "123"
        register_user_ui(
            driver, user,
            wait_for_element=RegistrationLocators.INVALID_PASSWORD
        )
        password_error = driver.find_element(
            *RegistrationLocators.INVALID_PASSWORD
        )
        assert password_error.is_displayed()
        assert password_error.text == "Некорректный пароль"

    def test_registration_empty_password_stays_on_page(self, driver):
        """
        Регистрация: при пустом пароле остаемся на странице регистрации
        """
        user = registration_user()
        user["password"] = ""
        register_user_ui(
            driver,
            user,
            wait_for_element=RegistrationLocators.HEADER_REGISTRATION
        )
        header = driver.find_element(
            *RegistrationLocators.HEADER_REGISTRATION
        )
        assert header.is_displayed()
        assert header.text == "Регистрация"
        assert driver.current_url == REGISTER_URL

    def test_registration_empty_email_stays_on_page(self, driver):
        """
        Регистрация: при пустом email остаемся на странице регистрации
        """
        user = registration_user()
        user["email"] = ""
        register_user_ui(
            driver,
            user,
            wait_for_element=RegistrationLocators.HEADER_REGISTRATION
        )
        header = driver.find_element(
            *RegistrationLocators.HEADER_REGISTRATION
        )
        assert header.is_displayed()
        assert header.text == "Регистрация"
        assert driver.current_url == REGISTER_URL

    def test_registration_existing_email_error(self, driver, registered_user):
        """
        Регистрация: ошибка при попытке зарегистрировать уже
        существующий email
        """
        register_user_ui(
            driver,
            registered_user,
            wait_for_element=RegistrationLocators.EXISTING_EMAIL_ERROR
        )
        existing_email_error = driver.find_element(
            *RegistrationLocators.EXISTING_EMAIL_ERROR
        )
        assert existing_email_error.is_displayed()
        assert existing_email_error.text == "Такой пользователь уже существует"
