from pages.base_methods import BasePage
from pages.locators import LoginPage, SignUpPage
from configs.data import DataParameters as Data
from configs.enums import GlobalErrorMessages
from pages.login_page import LoginMainPage
from selenium.webdriver.common.keys import Keys
import random
import string

class SignUpMainPage(BasePage):
    """ Методы для создания тестов по созданию нового пользователя"""

    def should_be_sign_up_page(self):
        """ Метод проверки корректного окна Sign up и его title"""
        self.do_click(LoginPage.SIGN_UP)
        self.assert_text_in_element(SignUpPage.PAGE_TITLE, Data.SIGN_UP_TITLE)
        assert self.get_page_title() == Data.SIGN_UP_PAGE_TITLE, \
            GlobalErrorMessages.WRONG_TITLE.value

    def should_be_country_selector(self):
        """ Метод проверки наличия селектора выбора страны """
        assert self.check_element(SignUpPage.COUNTRY_SELECTOR),\
            GlobalErrorMessages.WRONG_ELEMENT.value

    def should_be_date_input(self):
        """ Метод проверки наличия селектора выбора страны """
        assert self.check_element(SignUpPage.DATE_INPUT),\
            GlobalErrorMessages.WRONG_ELEMENT.value

    def should_be_sumbit_button(self):
        """ Метод проверки наличия кнопки 'Далее' """
        assert self.check_element(SignUpPage.FLOWSUBMIT),\
            GlobalErrorMessages.WRONG_ELEMENT.value

    def should_be_valid_sign_up_form(self):
        """ Метод проверки, что мы на нужной странце и есть все элементы на странице """
        self.should_be_sign_up_page()
        self.should_be_country_selector()
        self.should_be_date_input()
        self.should_be_sumbit_button()

    def select_random_country(self):
        """ Метод выбора рандомной страны """
        random_country = random.choice(list(SignUpPage.COUNTIES))
        country_locator = (SignUpPage.COUNTRY_CHOICE[0], SignUpPage.COUNTRY_CHOICE[1].format(random_country))
        self.do_click(country_locator)

    def generate_random_name(self):
        """ Метод генерации рандомного имени """
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 10)))
        print("Сгенерировано рандомное имя:", name)
        return name

    def generate_random_surname(self):
        """ Метод генерации рандомной фамилии """
        surname = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 10)))
        print("Сгенерирована рандомная фамилия:", surname)
        return surname

    def generate_random_phone(self):
        """ Метод генерации рандомного телефона """
        phone_digits = [random.randint(0, 9) for _ in range(10)]
        phone_number = f"+7{''.join(map(str, phone_digits))}"
        print("Сгенерирован рандомный номер:", phone_number)
        return phone_number

    def create_adult_user(self,):
        """ Метод проверки создания взрослого пользователя """
        self.do_click(SignUpPage.COUNTRY_SELECTOR)
        self.select_random_country()
        self.send_data(SignUpPage.DATE_INPUT, "01", "05", "2000")
        self.do_click(SignUpPage.FLOWSUBMIT)

        """ Проверка, что ввод возраста уже не нужен """
        self.check_element_disappeared(SignUpPage.DATE_INPUT)
        self.assert_query_parameter_in_url(Data.CREATE_FULL_USER_URL),\
            GlobalErrorMessages.WRONG_URL.value

        """ Генерация рандомных данных """
        name = self.generate_random_name()
        surename = self.generate_random_surname()
        phone = self.generate_random_phone()
        email = LoginMainPage.generate_email(self)

        self.send_keys(SignUpPage.INPUT_NAME, name)
        self.send_keys(SignUpPage.INPUT_LAST_NAME, surename)
        self.do_click(SignUpPage.FLOWSUBMIT)
        self.send_keys(SignUpPage.INPUT_PHONE, phone)
        self.send_keys(SignUpPage.INPUT_EMAIL, email)
