from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """ Все базовые методы для работы с элементами страниц,
        Включает в себе базовые методы клика, ввода текста, получение текса, атрибутов и т.д."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    @allure.title("Метод открытия/перехода на URL страницы")
    def open_page(self, url):
        self.driver.get(url)

    @allure.title("Метод получения title страницы")
    def get_page_title(self):
        print("Title страницы:", self.driver.title)
        return self.driver.title

    @allure.title("Метод клика по элементу")
    def do_click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    @allure.title("Метод ввода текста в элемент")
    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        element.send_keys(text)

    @allure.title("Метод ввода даты")
    def send_data(self, by_locator, dd, mm, yyyy):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        element.send_keys(dd, Keys.TAB, mm, Keys.TAB, yyyy)

    @allure.title("Метод фокусировки на элемент")
    def do_hover(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @allure.title("Метод клика и удержания клика на элменте")
    def do_hold(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).perform()
        actions.release(element).perform()

    @allure.title("Метод очистки текста из элемента")
    def do_clear_key(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        element.clear()

    @allure.title("Метод клика кнопки 'Enter' на поле")
    def do_enter_key(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        element.send_keys(Keys.ENTER)

    @allure.title("Метод получения текста из элемента")
    def get_element_text(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute('innerText')

    @allure.title("Метод проверки появления элмента на странице")
    def check_element(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            return False
        return True

    @allure.title("Метод проверки появления нескольких элементов на странице")
    def check_elements(self, by_locator, locator_value):
        try:
            self.wait.until(EC.presence_of_all_elements_located((by_locator, locator_value)))
        except TimeoutException:
            return False
        return True

    @allure.title("Метод проверки исчезновения элемента")
    def check_element_disappeared(self, by_locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(by_locator))
        except TimeoutException:
            return False
        return True

    @allure.title("Метод получения ссылки href из элемента")
    def get_element_href(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute('href')

    @allure.title("Метод получения свойства элемента")
    def get_element_property(self, by_locator, property):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        print(f"Свойство {property} элемента:", element.get_attribute(property))
        return element.get_attribute(property)

    @allure.title("Метод проверки, что элемент имеет определенное свойство")
    def assert_element_has_property(self, by_locator, property, expected_property):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        assert expected_property in element.get_attribute(property)

    @allure.title("Метод получения длины элемента или списка")
    def get_element_lenght(self, by_locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return len(elements)

    @allure.title("Метод проверки длины элемента")
    def assert_element_lenght(self, lenght, elem):
        assert len(elem) == lenght

    @allure.title("Метод проверки query-параметра в URL адресе")
    def assert_query_parameter_in_url(self, param):
        assert param in self.driver.current_url

    @allure.title("Метод проверки отсутствия query-параметра в URL адресе")
    def assert_query_parameter_not_in_url(self, param):
        assert param not in self.driver.current_url

    @allure.title("Метод получение списка URL элементов")
    def get_url_list(self, by_locator):
        url_list = []
        elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))

        for i in elements:
            url_list.append(i.get_attribute('href'))

        return url_list

    @allure.title("Метод проверки строки/текста в элементе")
    def assert_text_in_element(self, by_locator, text):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        assert text == element.text

    @allure.title("Метод проверки строки/текста в списке")
    def assert_text_in_list(self, by_locator, atribute, text):
        list_elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        list_links = []

        for item in list_elements:
            list_links.append(item.get_attribute({atribute}))

        for links in list_links:
            assert text in links

    @allure.title("Метод для проверки списка в списке")
    def assert_list_in_other_list(self, by_locator, list):
        list_elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        list_texts = []

        for element in list_elements:
            list_texts.append(element.get_attribute("innerText"))

        assert list == list_texts[:len(list)]

    @allure.title("Метод переключение между окнами браузера")
    def swap_to_next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.title("Метод переключения на предыдущее окно браузера")
    def swap_to_prev_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
