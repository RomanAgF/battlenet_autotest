class BaseElement:
    def __init__(self, driver, selector):
        self.driver = driver
        self.selector = selector
        def click(self):
            self.driver.finde_element(self.selector).click()


