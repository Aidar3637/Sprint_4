from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def click_order_button_top(self):
        self.click_element(By.CLASS_NAME, "Button_Button__ra12g")

    def check_logo_scooter(self):
        self.click_element(By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    def check_logo_yandex(self):
        self.click_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI")
