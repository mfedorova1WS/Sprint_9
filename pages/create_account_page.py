import allure
from pages.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators


class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def create_new_account(self, user_data):
        self.set_input(CreateAccountLocators.FIRST_NAME, user_data["first_name"])
        self.set_input(CreateAccountLocators.LAST_NAME, user_data["last_name"])
        self.set_input(CreateAccountLocators.USERNAME_INPUT, user_data["user_name"])
        self.set_input(CreateAccountLocators.EMAIL_INPUT, user_data["email"])
        self.set_input(CreateAccountLocators.PASSWORD_INPUT, user_data["password"])
        self.click_element(CreateAccountLocators.SUBMIT_BUTTON) # Нажимаем на кнопку "Создать аккаунт" в форме регистрации




