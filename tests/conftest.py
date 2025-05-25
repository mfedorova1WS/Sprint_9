import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import tempfile
import os
import shutil

def create_chrome_driver(headless=True) -> webdriver.Chrome:
    chrome_options = Options()

    if headless:
        chrome_options.add_argument('--headless=new')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=0')

    # Создание уникальной временной директории для профиля Chrome
    user_data_dir = tempfile.mkdtemp(prefix="chrome-profile-")
    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    # Сохраняем путь, чтобы потом удалить
    driver._user_data_dir = user_data_dir
    return driver


@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    with allure.step(f"Создаём драйвер Chrome (headless={headless})"):
        driver = create_chrome_driver(headless=headless)

    def fin():
        driver.quit()
        if hasattr(driver, "_user_data_dir") and os.path.exists(driver._user_data_dir):
            shutil.rmtree(driver._user_data_dir, ignore_errors=True)

    request.addfinalizer(fin)

    return driver



def pytest_addoption(parser):
    """Добавление кастомного параметра --headless."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode."
    )
