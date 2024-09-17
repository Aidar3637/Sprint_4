from .base_page import BasePage
from .locators import FAQPageLocators

class FAQPage(BasePage):

    def remove_obstructing_image(self):
        image_element = self.execute_script(
            "return document.querySelector('img[src=\"/assets/scooter.png\"]');"
        )
        if image_element:
            self.execute_script("arguments[0].remove();", image_element)

    def open_question(self, index):
        question_locator = FAQPageLocators.question_locator(index)
        self.scroll_to_element(*question_locator)
        self.click_element(*question_locator)

    def get_answer_text(self, index):
        answer_locator = FAQPageLocators.answer_locator(index)
        return self.get_element_text(*answer_locator)
