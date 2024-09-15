import sys
import pytest
import allure
# Добавляем путь к корневой папке проекта
sys.path.append('/Users/aidarshir/PycharmProjects/Sprint_4')

from page_objects.faq_page import FAQPage

@allure.feature("Раздел FAQ")
@allure.story("Проверка ответов на вопросы в разделе FAQ")
@pytest.mark.parametrize("question_index, expected_answer", [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])
@allure.title("Проверка вопросов FAQ")
@allure.description("Проверяем корректность отображения ответа на вопросы в разделе FAQ.")
def test_faq_answers(browser, question_index, expected_answer):
    faq_page = FAQPage(browser)
    faq_page.remove_obstructing_image()

    with allure.step(f"Открываем вопрос №{question_index}"):
        faq_page.open_question(question_index)
    with allure.step(f"Получаем ответ на вопрос №{question_index} и проверяем его"):
        actual_text = faq_page.get_answer_text(question_index)
        assert actual_text == expected_answer, f"Ожидался текст: '{expected_answer}', но получен: '{actual_text}'"
