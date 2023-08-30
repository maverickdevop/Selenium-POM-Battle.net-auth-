from tests.base_test import BaseTest
from pages.recover_password import RecoverPasswordMainPage
from configs.data import DataParameters as Data
import allure
import pytest


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Тесты на проверку работы регистрации нового пользователя')
class TestSignUp(BaseTest):

    def setup(self):
        self.recover = RecoverPasswordMainPage(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что мы попадаем на страницу Восстановления пароля')
    def test_should_be_on_recover_password_page(self):
        self.recover.open_page(Data.URL + "login/ru/")
        self.recover.should_be_recover_page()

    @pytest.mark.xfail(reason="Этот тест падает из-за появления капчи")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что мы можем восстановить пароль по email')
    def test_recover_pass_by_email(self):
        self.recover.open_page(Data.URL + "login/ru/")
        self.recover.possibility_to_recover_password()