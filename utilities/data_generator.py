from faker import Faker
import allure




class DataGenerator:

    @staticmethod
    def create_fake_user():
        """Метод для создания фейковых данных заказчика."""
        with allure.step("Создаём фейковые данные заказчика"):
            fake = Faker("ru_RU")
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            user_name = fake.user_name()
            email = fake.email()
            password = fake.password(length=10)

            user = {"first_name": first_name,
                    "last_name": last_name,
                    "user_name": user_name,
                    "email": email,
                    "password": password
                    }
            return user

    @staticmethod
    def create_random_comment():
        """Метод для создания случайного комментария длиной 100 символов"""
        with allure.step("Создаём случайный комментарий"):
            fake = Faker("ru_RU")
            # Генерируем текст и обрезаем до 100 символов
            comment = fake.text(max_nb_chars=100)
            # Убедимся, что длина точно 100 символов
            return comment[:100]

    @staticmethod
    def generator_uid():
        with allure.step("Генерируем uid"):
            """Метод для генерации uid"""
            fake = Faker()
            uid = fake.uuid4()
            return uid
