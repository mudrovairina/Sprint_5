import pytest
from selenium import webdriver

from auth_helpers import register_user_ui
from user_generator import registration_user


@pytest.fixture
def driver():
    """Фикстура для запуска браузера Chrome"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    """Фикстура для создания зарегистрированного пользователя"""
    user = registration_user()
    register_user_ui(driver, user)
    return user
