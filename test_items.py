from selenium.common.exceptions import NoSuchElementException


class TestSwitchLanguages:

    def test_check_visible_button_add_to_basket(self, browser, request):
        lang = request.config.getoption("language")
        link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"

        browser.get(link)
        try:
            assert browser.find_element_by_css_selector('form#add_to_basket_form button')
        except NoSuchElementException:
            assert False, "Кнопка не найдена!"


