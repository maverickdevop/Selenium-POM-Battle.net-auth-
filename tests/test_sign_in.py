from tests.base_test import BaseTest
from pages.sign_in_page import SignUpMainPage
from configs.data import DataParameters as Data
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Тесты на проверку работы регистрации нового пользователя')
class TestLogin(BaseTest):

    def setup(self):
        self.signup = SignUpMainPage(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что мы попадаем на страницу Sign Up')
    def test_should_be_on_sign_up_page(self):
        self.signup.open_page(Data.URL + "login/ru/")
        self.signup.should_be_valid_sign_up_form()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка создания взрослого пользователя')
    def test_create_adult_user(self):
        self.signup.open_page(Data.URL_NEW_USER + "creation/flow/creation-full")
        self.signup.create_adult_user()
