import os
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from data.data import BaseData as Bd
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Bd.TIMEOUT)

    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ищем элементы по {locator}')
    def find_elements(self, locator):
        try:
            return self.wait.until(Ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    @allure.step('Ищем элемент по {locator}')
    def find_element(self, locator):
        return self.wait.until(Ec.presence_of_element_located(locator))

    @allure.step('Ждем, пока элемент {locator} станет видимым')
    def wait_for_load(self, locator):
        return self.wait.until(Ec.visibility_of_element_located(locator))

    @allure.step('Ждем, пока элемент {locator} станет кликабельным')
    def wait_for_click(self, locator):
        return self.wait.until(Ec.element_to_be_clickable(locator))

    @allure.step('Получаем текст элемента по локатору {locator}')
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Проверяем отображение элемента {locator}')
    def check_is_displayed(self, locator):
        try:
            self.wait_for_load(locator)
            return self.driver.find_element(*locator).is_displayed()
        except TimeoutException:
            raise AssertionError(f"Элемент с локатором {locator} не найден на странице.")

    @allure.step('Кликаем на элемент {locator}')
    def click_element(self, locator):
        try:
            self.wait_for_click(locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            raise AssertionError(f"Не удалось кликнуть на элемент {locator}: {e}")

    @allure.step('Кликаем JS на элемент {locator}')
    def click_element_js(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            raise AssertionError(f"Не удалось выполнить JS-клик по элементу {locator}: {e}")

    @allure.step('Вводим текст "{set_data}" в поле {locator}')
    def set_input(self, locator, set_data):
        element = self.wait_for_click(locator)
        element.clear()
        element.send_keys(set_data)

    @allure.step('Загружаем изображение {file_path}')
    def upload_image(self, locator, file_path):
        if not os.path.isabs(file_path):
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не обнаружен: {file_path}")

        self.find_element(locator).send_keys(file_path)
        return os.path.basename(file_path)
