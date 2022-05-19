from selenium import webdriver
from pages.basepage import BasePage
from locators.portal.login_locators import LoginpageLocators
from locators.portal.home_locators import HomepageLocators

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

    def change_password_check(self):
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass

    def logout(self): 
        self.click(HomepageLocators.LOGOUT)   