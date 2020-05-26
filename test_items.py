from selenium.common.exceptions import NoSuchElementException
import time


class TestSwitchLanguages:

    def test_check_visible_button_add_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        browser.get(link)
        time.sleep(30)
        try:
            assert browser.find_element_by_css_selector('form#add_to_basket_form button')
        except NoSuchElementException:
            assert False, "Кнопка не найдена!"


