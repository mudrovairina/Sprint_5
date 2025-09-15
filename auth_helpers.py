from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import CommonAuthLocators, LoginLocators, RegistrationLocators
from urls import REGISTER_URL


def register_user_ui(driver, user, wait_for_element=None):
    """
    Создает пользователя через форму регистрации.
    Если указан wait_for_header,
    ждет появления этого элемента после нажатия кнопки регистрации.
    """
    driver.get(REGISTER_URL)
    driver.find_element(
        *RegistrationLocators.INPUT_NAME
    ).send_keys(user["name"])
    driver.find_element(
        *CommonAuthLocators.INPUT_EMAIL
    ).send_keys(user["email"])
    driver.find_element(
        *CommonAuthLocators.INPUT_PASSWORD
    ).send_keys(user["password"])
    driver.find_element(*RegistrationLocators.BUTTON_REGISTER).click()

    if wait_for_element:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(wait_for_element)
        )

def login(driver, registered_user, wait_for_element=None):
    """Заполняет форму логина и проверяет успешный вход"""
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(CommonAuthLocators.HEADER_LOGIN)
    )
    driver.find_element(
        *CommonAuthLocators.INPUT_EMAIL
    ).send_keys(registered_user["email"])
    driver.find_element(
        *CommonAuthLocators.INPUT_PASSWORD
    ).send_keys(registered_user["password"])
    driver.find_element(*LoginLocators.BUTTON_SUBMIT_LOGIN).click()
    if wait_for_element:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(wait_for_element)
        )
