from selenium.webdriver.common.by import By

# Локаторы для FAQPage
class FAQPageLocators:
    SCOOTER_IMAGE = (By.CSS_SELECTOR, 'img[src="/assets/scooter.png"]')

    @staticmethod
    def question_locator(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")


# Локаторы для OrderPage
class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.CLASS_NAME, 'select-search__input')
    METRO_OPTION = lambda metro: (By.XPATH, f'//div[text()="{metro}"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.CLASS_NAME, 'Button_Middle__1CSJM')
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    ORDER_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    RENTAL_PERIOD_OPTION = (By.XPATH, '//div[text()="сутки"]')
    SCOOTER_COLOR = (By.XPATH, '//label[contains(text(), "серая безысходность")]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_POPUP = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    STATUS_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Посмотреть статус"]')

# Локаторы для HomePage
class HomePageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")