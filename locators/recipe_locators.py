from selenium.webdriver.common.by import By


class RecipeLocators:
    # Заголовок рецепта
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card')]")

    # Заголовок формы
    FORM_TITLE = (By.XPATH, "//h1[text()='Создание рецепта']")

    #Навигация
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes' and @aria-current='page']")
    SUBSCRIPTIONS_LINK = (By.XPATH, "//a[@href='/subscriptions']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")
    FAVORITES_LINK = (By.XPATH, "//a[@href='/favorites']")
    CART_LINK = (By.XPATH, "//a[@href='/cart']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_menuLink') and text()='Выход']")

    # Основные поля
    RECIPE_NAME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField') and preceding-sibling::div[text()='Название рецепта']]")
    COOKING_TIME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField') and preceding-sibling::div[contains(text(), 'Время приготовления')]]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField')]")

    # Теги рецепта
    TAG_BREAKFAST = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Завтрак']]")
    TAG_LUNCH = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Обед']]")
    TAG_DINNER = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Ужин']]")

    # Ингредиенты
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")
    INGREDIENTS_DROPDOWN = (By.XPATH, "//div[contains(@class, 'styles_container')]/div") # Список ингредиентов
    INGREDIENT_DROPDOWN_ITEM = (By.XPATH, "//div[contains(@class, 'styles_container')]/div")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd') and text()='Добавить ингредиент']")

    # Загрузка изображения
    IMAGE_UPLOAD_INPUT = (By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput')]")
    IMAGE_UPLOAD_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_button') and text()='Выбрать файл']")

    # Кнопка создания рецепта
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_button') and contains(text(), 'Создать рецепт')]")

    # Добавленные ингредиенты
    ADDED_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'styles_ingredientsAdded')]//div[contains(@class, 'styles_ingredientItem')]")