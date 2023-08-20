from .base_element import BaseElement

class TextFieldElement(BaseElement):
    def __init__(self, driver, selector):
        super().__init__(driver, selector)


    def __enter__(self, text):
        element = self.driver.find_element(self.selector)
        element.clear()
        element.send_keys(text)