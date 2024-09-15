from selenium.webdriver.common.by import By
from .base_page import BasePage

class FAQPage(BasePage):

    def remove_obstructing_image(self):
        image_element = self.browser.execute_script(
            "return document.querySelector('img[src=\"/assets/scooter.png\"]');")
        if image_element:
            self.browser.execute_script("arguments[0].remove();", image_element)

    def open_question(self, index):
        question_locator = (By.ID, f"accordion__heading-{index}")
        self.scroll_to_element(*question_locator)
        self.click_element(*question_locator)

    def get_answer_text(self, index):
        answer_locator = (By.ID, f"accordion__panel-{index}")
        answer = self.find_element(*answer_locator)
        return answer.text
