import allure
from utilities.data_generator import DataGenerator
from data.data import DataForAuth
from pages.create_recipe_page import CreateRecipe
from pages.auth_page import AuthPage
from locators.recipe_locators import RecipeLocators


@allure.feature("Рецепты")
@allure.story("Создание рецептов")
class TestCreateRecipe:

    @allure.title('Создание рецепта')
    def test_create_recipe(self, driver):
        create_recipes = CreateRecipe(driver)
        auth_page = AuthPage(driver)

        with allure.step("Подготовка тестовых данных"):
            comment = DataGenerator.create_random_comment()
            image_path = "data/omlet.jpg"
            uid = DataGenerator.generator_uid()
            recipe_name = f"Омлет с лисичками {uid}"

        with allure.step("Авторизация пользователя"):
            auth_page.open(DataForAuth.BASE_URL)
            auth_page.auth(DataForAuth.NAME, DataForAuth.PASSWORD)

        with allure.step("Создание нового рецепта"):
            create_recipes.click_element(RecipeLocators.CREATE_RECIPE_LINK)

            with allure.step("Заполнение основных данных"):
                create_recipes.set_input(RecipeLocators.RECIPE_NAME_INPUT, recipe_name)
                create_recipes.click_element(RecipeLocators.TAG_DINNER)
                create_recipes.set_input(RecipeLocators.COOKING_TIME_INPUT, 15)
                create_recipes.set_input(RecipeLocators.DESCRIPTION_TEXTAREA, comment)

            with allure.step("Добавление ингредиентов"):
                ingredients = [
                    ("яйца куриные", 500),
                    ("лисички", 6),
                    ("соль", 30)
                ]
                for name, amount in ingredients:
                    create_recipes.add_ingredient(name, amount)

            with allure.step("Загрузка картинки"):
                create_recipes.upload_image(RecipeLocators.IMAGE_UPLOAD_INPUT, image_path)

            with allure.step("Отправка формы"):
                create_recipes.click_element(RecipeLocators.SUBMIT_BUTTON)

        with allure.step("Проверка создания рецепта"):
            title_recipes_text = create_recipes.get_element_text(RecipeLocators.RECIPE_TITLE)
            assert uid in title_recipes_text, (
                f"Ожидалось найти ID '{uid}' в названии рецепта, "
                f"получено: '{title_recipes_text}'"
            )