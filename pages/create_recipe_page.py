from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from locators.recipe_locators import RecipeLocators


class CreateRecipe(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Добавляем ингредиенты ')
    def add_ingredient(self, name_ingredient, amount):
        self.set_input(RecipeLocators.INGREDIENT_INPUT, name_ingredient)
        locator = (By.XPATH, f"//div[contains(@class, 'styles_container')]/div[contains(text(), '{name_ingredient}')]")
        self.click_element_js(locator)
        self.set_input(RecipeLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click_element(RecipeLocators.ADD_INGREDIENT_BUTTON)




