from selenium import webdriver
from pages.basepage import BasePage
from locators.portal.login_locators import LoginpageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(LoginpageLocators.PATH)

    def login_success(self): 
        self.send_keys(LoginpageLocators.ID, "wtwt")
        self.send_keys(LoginpageLocators.PASSWORD, "webzen@1")
        self.click(LoginpageLocators.LOGIN_BUTTON)     
    
    def login_fail(self): 
        self.send_keys(LoginpageLocators.ID, "wtwt")
        self.send_keys(LoginpageLocators.PASSWORD, "1111")
        self.click(LoginpageLocators.LOGIN_BUTTON)     