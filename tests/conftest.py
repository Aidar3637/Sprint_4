import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    # Запуск браузера
    driver = webdriver.Firefox()
    # Открытие страницы
    driver.get("https://qa-scooter.praktikum-services.ru/")
    # Передаем инстанс драйвера в тесты
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()