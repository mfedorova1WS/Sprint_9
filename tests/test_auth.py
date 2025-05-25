import allure
from data.data import DataForAuth
from locators.recipe_locators import RecipeLocators
from pages.auth_page import AuthPage


@allure.feature("Авторизация")
@allure.story("Авторизации пользователя")
class TestAuth:

    @allure.title('Авторизация в Продуктовом помощнике')
    def test_auth_login(self, driver):
        with allure.step("Инициализация страницы"):
            auth_page = AuthPage(driver)

        with allure.step("Открытие страницы авторизации"):
            auth_page.open(DataForAuth.BASE_URL)

        with allure.step("Авторизация"):
            auth_page.auth(DataForAuth.NAME, DataForAuth.PASSWORD)

        with allure.step("Проверка успешной авторизации"):
            assert auth_page.check_is_displayed(RecipeLocators.LOGOUT_BUTTON), "Кнопка 'Выход' не отображается после авторизации"