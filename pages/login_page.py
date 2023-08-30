from pages.base_methods import BasePage
from pages.locators import LoginPage
from configs.data import DataParameters as Data
from configs.enums import GlobalErrorMessages
import random
import string

class LoginMainPage(BasePage):
    """ Методы для создания тестов по авторизации"""

    def should_be_login_page(self):
        """ Метод проверки корректного окна логина и title"""
        self.check_element(LoginPage.PAGE_TITLE)
        self.assert_text_in_element(LoginPage.PAGE_TITLE, Data.LOGIN_TITLE)
        assert self.get_page_title() == Data.LOGIN_PAGE_TITLE,\
            GlobalErrorMessages.WRONG_TITLE.value

    def should_be_email_input(self):
        """ Метод проверки наличия инпута Email/Логина """
        self.check_element(LoginPage.INPUT_LOGIN)

    def should_be_password_input(self):
        """ Метод проверки наличия инпута пароля """
        self.check_element(LoginPage.INPUT_PASSWORD)

    def should_be_sumbit_button(self):
        """ Метод проверки наличия кнопки 'Авторизироваться' """
        self.check_element(LoginPage.SUBMIT_BTN)

    def should_be_valid_login_form(self):
        """ Метод проверки, что мы на нужной странце и есть все элементы на странице """
        self.should_be_login_page()
        self.should_be_email_input()
        self.should_be_password_input()
        self.should_be_sumbit_button()

    def should_be_other_login_methods(self):
        """ Метод проверки других типов авторизации через Google, Apple ... """
        for auth_name, auth_locator in LoginPage.AUTHS.items():
            self.check_elements(*auth_locator)

    def generate_email(self):
        """ Метод генерации рандомного email"""
        email_prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return f"{email_prefix}@gmail.com"

    def generate_password(self):
        """ Метод генерации рандомного пароля"""
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return password

    def do_login(self, username, password):
        """ 1. Метод ввода валидных данных
            2. Проверка наличия кнопки'Авторизироваться' """
        self.send_keys(LoginPage.INPUT_LOGIN, username)
        self.send_keys(LoginPage.INPUT_PASSWORD, password)
        self.check_element(LoginPage.SUBMIT_BTN)

    def watch_input_pass_and_lenght(self, password):
        """ 1. Метод проверки просмотра пароля
            2. Клик на курсор элемента-кнопки
            3. Проверка длины пароля в репитере """
        self.send_keys(LoginPage.INPUT_PASSWORD, password)
        try:
            self.do_click(LoginPage.WATCH_PASSWORD_BTN)
            pass_lenght = self.get_element_property(LoginPage.INPUT_PASSWORD, "data-charmax-counter")\
                .replace("/128")
            self.assert_element_lenght(8, pass_lenght)

        except Exception:
            return False