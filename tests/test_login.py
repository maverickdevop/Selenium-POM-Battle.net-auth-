from tests.base_test import BaseTest
from pages.login_page import LoginMainPage
from configs.data import DataParameters as Data
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Тесты на проверку работы авторизации на сайте')
class TestLogin(BaseTest):

    def setup(self):
        self.login = LoginMainPage(self.driver)
        self.login.open_page(Data.URL + "login/ru/")
        self.driver.implicitly_wait(5)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что мы попадаем на страницу авторизации')
    def test_should_be_on_login_page(self):
        self.login.should_be_valid_login_form()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка наличия других методов авторизации на странице')
    def test_should_be_other_login_methods(self):
        self.login.should_be_other_login_methods()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка логина с использованием рандомных данных')
    def test_random_data_login(self):
        self.login.do_login(self.login.generate_email(), self.login.generate_password())

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка дублирования/просмотра пароля в поле')
    def test_watch_password(self):
        self.login.watch_input_pass_and_lenght(self.login.generate_password())