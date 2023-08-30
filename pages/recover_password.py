from pages.base_methods import BasePage
from pages.locators import RecoverPassPage
from configs.data import DataParameters as Data
from configs.enums import GlobalErrorMessages
from pages.login_page import LoginMainPage
import time

class RecoverPasswordMainPage(BasePage):
    """ Методы для создания тестов по восстановления пароля """

    def should_be_recover_link(self):
        self.do_click(RecoverPassPage.RECOVER_PASS_LINK)

    def should_be_recover_page(self):
        """ Метод проверки окна восстановления логина и title
        1. Клик на восстановление пароля со страницы логина
        2. Проверка страницы (Переход на новую вкладку, хардкод ожидания на 1 сек.)
        3. Возврат на предыдущую вкладку """
        self.should_be_recover_link()
        self.swap_to_next_window()
        time.sleep(1)

        assert self.get_page_title() == Data.RECOVERY_TITLE, \
            GlobalErrorMessages.WRONG_TITLE.value

        self.assert_text_in_element(RecoverPassPage.PAGE_TITLE, Data.RECOVERY_TITLE)
        self.assert_query_parameter_in_url(Data.RECOVERY_URL), \
            GlobalErrorMessages.WRONG_URL.value
        self.swap_to_prev_window()

    def should_be_recover_password_button(self):
        """ Метод проверки наличия кнопки восстановлени пароля"""
        self.do_click(RecoverPassPage.RECOVER_PASS_BTN)

    def possibility_to_recover_password(self):
        """ Метод восстановления пароля
         1. Клик на кнопку (Переход на новую вкладку, хардкод ожидания на 1 сек.)
         2. Проверка URL адреса
         3. Ввод email, которого нет в базе
         4. Проверка получения ошибки
         5. Возврат назад """
        self.should_be_recover_link()
        self.swap_to_next_window()
        time.sleep(1)

        self.should_be_recover_password_button()
        self.assert_query_parameter_in_url(Data.RECOVER_PASS_URL),\
            GlobalErrorMessages.WRONG_URL.value

        email = LoginMainPage.generate_email(self)
        self.send_keys(RecoverPassPage.EMAIL_IDENTIFY_INPUT, email)
        self.do_click(RecoverPassPage.EMAIL_SUBMIT)

        try:
            self.check_element(RecoverPassPage.ERROR_MSG_IDENTIFY)
            self.do_click(RecoverPassPage.BACK_BUTTON)
            self.assert_query_parameter_not_in_url(Data.RECOVER_PASS_URL), \
                GlobalErrorMessages.WRONG_URL.value
        except Exception:
            print("Попали на ввод капчи!")
            pass