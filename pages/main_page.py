from ..elements.button_element import ButtonElement


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_with_google_button = ButtonElement(driver, '#google')
        self.login_with_facebook_button = ButtonElement(driver, '#facebook')

    def is_open(self):
        return self.driver.current_url == 'https://eu.account.battle.net/login/ru/'
