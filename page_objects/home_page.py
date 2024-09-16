from .locators import HomePageLocators
from .base_page import BasePage

class HomePage(BasePage):
    def click_order_button_top(self):
        self.click_element(*HomePageLocators.ORDER_BUTTON_TOP)

    def check_logo_scooter(self):
        # Клик по логотипу "Самоката" и проверка URL
        self.click_element(*HomePageLocators.SCOOTER_LOGO)
        self.assert_url("https://qa-scooter.praktikum-services.ru/", "Не удалось перейти на главную страницу 'Самоката'")

    def check_logo_yandex(self):
        # Клик по логотипу Яндекса
        original_window = self.browser.current_window_handle
        self.click_element(*HomePageLocators.YANDEX_LOGO)

        # Переключение на новое окно
        self.switch_to_new_window(original_window)

        # Проверка, что открылся Дзен через редирект
        self.assert_url_contains("https://dzen.ru/", "Не удалось перейти на страницу Дзена")

        # Возвращение на исходное окно
        self.browser.switch_to.window(original_window)