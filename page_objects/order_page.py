from .locators import OrderPageLocators
from .base_page import BasePage

class OrderPage(BasePage):
    def fill_order_form(self, data):
        # Имя
        self.find_element(*OrderPageLocators.NAME_INPUT).send_keys(data["name"])

        # Фамилия
        self.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(data["surname"])

        # Адрес
        self.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(data["address"])

        # Станция метро
        self.click_element(*OrderPageLocators.METRO_INPUT)
        self.click_element(*OrderPageLocators.METRO_OPTION(data["metro"]))

        # Телефон
        self.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(data["phone"])

        # Клик по кнопке "Далее"
        self.click_element(*OrderPageLocators.NEXT_BUTTON)

        # Дата
        self.find_element(*OrderPageLocators.DATE_INPUT).send_keys(data["date"])
        self.click_element(*OrderPageLocators.ORDER_HEADER)

        # Выбор срока аренды
        self.click_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(*OrderPageLocators.RENTAL_PERIOD_OPTION)

        # Выбор цвета самоката
        self.click_element(*OrderPageLocators.SCOOTER_COLOR)

        # Комментарий для курьера
        self.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(data["comment"])

        # Клик по кнопке "Заказать"
        self.click_element(*OrderPageLocators.ORDER_BUTTON)

        # Подтверждение заказа
        self.click_element(*OrderPageLocators.CONFIRM_BUTTON)

    def check_success_popup(self):
        success_popup = self.find_element(*OrderPageLocators.SUCCESS_POPUP)
        assert success_popup.is_displayed(), "Заказ оформлен"

        # Нажатие на кнопку "Посмотреть статус"
        self.click_element(*OrderPageLocators.STATUS_BUTTON)