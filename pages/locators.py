""" Локаторы для сех страниц
    В теством молько для страницы логина и авторизации """

from selenium.webdriver.common.by import By


class LoginPage:

    PAGE_LOGO = (By.CSS_SELECTOR, "h1.logo.logo-horizontal.logo-small")
    PAGE_TITLE = (By.XPATH, "//h3[@id='login-header']")

    AUTHS = {
        'GOOGLE_AUTH': (By.XPATH, "//button[@id='google']"),
        'FACEBOOK_AUTH': (By.XPATH, "//button[@id='facebook']"),
        'APPLE_AUTH': (By.XPATH, "//button[@id='apple']"),
        'LIVE_AUTH': (By.XPATH, "//button[@id='live']"),
        'PSN_AUTH': (By.XPATH, "//button[@id='psn']"),
        'NINTENDO_AUTH': (By.XPATH, "//button[@id='nintendo']"),
        'STEAM_AUTH': (By.XPATH, "//button[@id='steam']")
    }

    INPUT_LOGIN = (By.XPATH, "//input[@id='accountName']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='password']")
    WATCH_PASSWORD_BTN = (By.XPATH, "//span[@class='view-password-button']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='submit']")

    SIGN_UP = (By.XPATH, "//a[@id='signup']")
    LOGIN_SUPPORT = (By.XPATH, "//a[@id='loginSupport']")

class SignUpPage:

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.step__title.step__block")

    ERROR_LABEL = (By.XPATH, "//li[@class='step__field-errors-item']")
    ICON_SUCCESS = (By.XPATH, "//div[@class='step-icon--success']")
    FLOWSUBMIT = (By.XPATH, "//button[@id='flow-form-submit-btn']")

    COUNTRY_SELECTOR = (By.XPATH, "//select[@id='capture-country']")
    COUNTIES = {'AUT', 'CYP', 'FIN', 'CHE'}
    COUNTRY_CHOICE = (By.XPATH, "//option[@value='{}']")

    DATE_INPUT = (By.XPATH, "//input[@name='dob-plain']")

    INPUT_NAME = (By.XPATH, "//input[@id='capture-first-name']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@id='capture-last-name']")

    INPUT_EMAIL = (By.XPATH, "//input[@id='capture-email']")
    INPUT_PHONE = (By.XPATH, "//input[@id='capture-phone-number']")