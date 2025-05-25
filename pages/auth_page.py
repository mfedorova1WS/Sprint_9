import allure
from pages.base_page import BasePage
from locators.auth_page_locators import AuthLocators as Al


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Авторизация ')
    def auth(self, user_email, user_password):
        self.set_input(Al.EMAIL, user_email)
        self.set_input(Al.PASSWORD, user_password)
        self.click_element(Al.SUBMIT_BUTTON)

