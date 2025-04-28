from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class SearchProduct(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button')
    PRODUCT_NAME = (By.CLASS_NAME, 'poly-component__title')
    

    def search(self, product_name):
        self.enter_text(self.SEARCH_FIELD, product_name)
        self.click(self.SEARCH_BUTTON)
        
    def isElementPresent(self):
        elmento = self.find_element(self.PRODUCT_NAME)
        texto = elmento.text
        return texto
