from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
    def fill_order_form(self, data):
        # Имя
        self.find_element(By.XPATH, '//input[@placeholder="* Имя"]').send_keys(data["name"])

        # Фамилия
        self.find_element(By.XPATH, '//input[@placeholder="* Фамилия"]').send_keys(data["surname"])

        # Адрес
        self.find_element(By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]').send_keys(data["address"])

        # Станция метро
        self.click_element(By.CLASS_NAME, 'select-search__input')
        self.click_element(By.XPATH, f'//div[text()="{data["metro"]}"]')

        # Телефон
        self.find_element(By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]').send_keys(data["phone"])

        # Клик по кнопке "Далее"
        self.click_element(By.CLASS_NAME, 'Button_Middle__1CSJM')

        # Дата
        self.find_element(By.XPATH, '//input[@placeholder="* Когда привезти самокат"]').send_keys(data["date"])
        self.click_element(By.XPATH, '//div[@class="Order_Header__BZXOb"]')

        # Выбор срока аренды
        self.click_element(By.CLASS_NAME, 'Dropdown-control')
        self.click_element(By.XPATH, '//div[text()="сутки"]')

        # Выбор цвета самоката
        self.click_element(By.XPATH, '//label[contains(text(), "серая безысходность")]')

        # Комментарий для курьера
        self.find_element(By.XPATH, '//input[@placeholder="Комментарий для курьера"]').send_keys(data["comment"])

        # Клик по кнопке "Заказать"
        self.click_element(By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')

        # Подтверждение заказа
        self.click_element(By.XPATH, '//button[text()="Да"]')

    def check_success_popup(self):
        success_popup = self.find_element(By.CLASS_NAME, 'Order_Modal__YZ-d3')
        assert success_popup.is_displayed(), "Заказ оформлен"

        # Нажатие на кнопку "Посмотреть статус"
        self.click_element(By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Посмотреть статус"]')
