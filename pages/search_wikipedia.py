from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class Search(BasePage):
    SEARCH_FIELD = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/div/div[1]/input')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    SEARCH_FIRST_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/a')
    TITLE = (By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1/span')
    

    def search(self, search_text):
        self.click(self.SEARCH_FIRST_BUTTON)
        self.enter_text(self.SEARCH_FIELD, search_text)
        self.click(self.SEARCH_BUTTON)
        
    def isElementPresent(self):
        elmento = self.find_element(self.TITLE)
        texto = elmento.text
        return texto
