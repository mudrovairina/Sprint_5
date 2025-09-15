from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import ConstructorTabsLocators
from urls import BASE_URL


class TestConstructor:
    def test_go_to_section_buns(self, driver):
        driver.get(BASE_URL)
        buns_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                ConstructorTabsLocators.BUNS_HEADER
            )
        )
        assert buns_header.is_displayed()
        assert 'Булки' in buns_header.text

    def test_go_to_section_sauces(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ConstructorTabsLocators.SAUCES_TAB).click()
        sauces_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                ConstructorTabsLocators.SAUCES_HEADER
            )
        )
        assert sauces_header.is_displayed()
        assert 'Соусы' in sauces_header.text

    def test_go_to_section_fillings(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ConstructorTabsLocators.FILLINGS_TAB).click()
        fillings_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                ConstructorTabsLocators.FILLINGS_HEADER
            )
        )
        assert fillings_header.is_displayed()
        assert 'Начинки' in fillings_header.text
