from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, by, value, timeout=4):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, by, value, timeout=4):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def scroll_to_element(self, by, value, timeout=4):
        element = self.find_element(by, value, timeout)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_text(self, by, value, timeout=4):
        element = self.find_element(by, value, timeout)
        return element.text

    def execute_script(self, script):
        self.browser.execute_script(script)
