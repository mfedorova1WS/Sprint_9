import allure
from data.data import DataForAuth as DataForAuth
from pages.create_account_page import CreateAccountPage
from locators.auth_page_locators import AuthLocators
from utilities.data_generator import DataGenerator


@allure.feature("Регистрация")
@allure.story("Регистрации пользователя")
class TestCreateAccount:

    @allure.title('Регистрация нового пользователя')
    def test_registration_user(self, driver):
        with allure.step("Инициализация страницы"):
            registration_page = CreateAccountPage(driver)

        with allure.step("Генерация тестовых данных пользователя"):
            fake_user = DataGenerator.create_fake_user()

        with allure.step("Открытие страницы авторизации"):
            registration_page.open(DataForAuth.BASE_URL)

        with allure.step("Переход на страницу регистрации"):
            registration_page.click_element(AuthLocators.SIGNUP_BUTTON)

        with allure.step("Заполнение формы регистрации"):
            registration_page.create_new_account(fake_user)

        with allure.step("Проверка успешной регистрации"):
            assert registration_page.check_is_displayed(
                AuthLocators.FORM_TITLE), "Форма авторизации не отображается после регистрации"