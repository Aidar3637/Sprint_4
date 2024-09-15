import pytest
import sys
import allure
# Добавляем путь к корневой папке проекта
sys.path.append('/Users/aidarshir/PycharmProjects/Sprint_4')

from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage

@allure.feature("Оформление заказа")
@allure.story("Пользователь может оформить заказ")
class TestOrderFlow:
    @pytest.mark.parametrize("order_data", [
        {"name": "Иван", "surname": "Иванов", "address": "ул. Пушкина, д. 10", "metro": "Черкизовская",
         "phone": "+79991234567", "date": "31.12.2024", "comment": "Позвоните за час до доставки", "color": "black"},
        {"name": "Петр", "surname": "Петров", "address": "ул. Ленина, д. 5", "metro": "Текстильщики",
         "phone": "+79998765432", "date": "01.01.2025", "comment": "Доставьте утром", "color": "grey"}
    ])
    @allure.title("Тест оформления заказа с разными данными")
    @allure.description("Тест проверяет процесс оформления заказа на самокат с использованием различных наборов данных")
    @allure.link("https://jira.project.com/browse/PROJECT-123", name="Таск в Jira")
    def test_order_flow(self, browser, order_data):
        with allure.step("Кликаем на кнопку Заказать в верхней части страницы"):
            home_page = HomePage(browser)
            home_page.click_order_button_top()

        with allure.step("Заполняем форму заказа"):
            order_page = OrderPage(browser)
            order_page.fill_order_form(order_data)

        with allure.step("Проверяем успешное создание заказа"):
            order_page.check_success_popup()

        with allure.step("Проверяем кликабельность логотипов"):
            home_page.check_logo_scooter()
            home_page.check_logo_yandex()