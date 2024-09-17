from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def assert_url(self, expected_url, error_message, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.url_contains(expected_url))
        assert self.browser.current_url == expected_url, error_message

    def assert_url_contains(self, expected_url_part, error_message, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.url_contains(expected_url_part))
        assert expected_url_part in self.browser.current_url, error_message

    def switch_to_new_window(self, original_window, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.browser.window_handles if window != original_window][0]
        self.browser.switch_to.window(new_window)

    def get_current_window_handle(self):
        return self.browser.current_window_handle

    def switch_to_window(self, window_handle):
        self.browser.switch_to.window(window_handle)