import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    """ Фикстура для инициализации драйвера """

    # Установим опции по умолчанию None и параметр опции
    options = None
    browser_name = request.config.getoption('browser')

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-cache")
        options.add_argument("--window-size=1200,700")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver = driver

    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = driver

    else:
        raise ValueError("Неподдерживаемый браузер: {}".format(browser_name))

    yield
    driver.delete_all_cookies()
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox', help="Выбор драйвера Chrome или Firefox")