from selenium import webdriver
from locators.muignition2.home_locators import Mui2pageLocators
from pages.basepage import BasePage
from locators.muignition2.cs_locators import Mui2CSLocators
from locators.portal.login_locators import LoginpageLocators

class CSPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(LoginpageLocators.PATH)

    def login_success(self): 
        self.send_keys(LoginpageLocators.ID, "rfrf")
        self.send_keys(LoginpageLocators.PASSWORD, "webzen@1")
        self.click(LoginpageLocators.LOGIN_BUTTON)     

    def open_cs_page(self):
        self.open_url(Mui2CSLocators.PATH)

    def cs_write(self):
        self.send_keys(Mui2CSLocators.PHONE, '92779710')
        self.send_keys(Mui2CSLocators.TITLE, '안녕하세요')
        self.send_keys(Mui2CSLocators.CONTENT, '반갑습니다')
        self.click(Mui2CSLocators.AGRPRIVACY)
        self.click(Mui2CSLocators.WRITE)