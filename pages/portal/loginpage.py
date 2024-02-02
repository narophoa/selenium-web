from selenium import webdriver
from pages.basepage import BasePage
from locators.portal.login_locators import LoginpageLocators
from locators.portal.home_locators import HomepageLocators
from config.config import ID, PW, ID2, PW2, WRONG_PW

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(LoginpageLocators.PATH)

    def login_success(self): 
        self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, ID)
        self.send_keys(LoginpageLocators.PASSWORD, PW)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass

    def login_success2(self): 
        self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, ID2)
        self.send_keys(LoginpageLocators.PASSWORD, PW2)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass
    
    def login_fail(self): 
        self.send_keys(LoginpageLocators.ID, ID)
        self.send_keys(LoginpageLocators.PASSWORD, WRONG_PW)
        self.click(LoginpageLocators.LOGIN_BUTTON)     

    def logout(self): 
        self.click(HomepageLocators.LOGOUT)   