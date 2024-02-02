from selenium import webdriver
from pages.basepage import BasePage
from locators.shotonline.login_locators import LoginpageLocators
from locators.shotonline.home_locators import ShotpageLocators
from config.config import SHOTID, SHOTPW

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(LoginpageLocators.PATH)

    def login_success(self): 
        self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, SHOTID)
        self.send_keys(LoginpageLocators.PASSWORD, SHOTPW)
        self.click(LoginpageLocators.LOGIN_BUTTON)       

    def logout(self): 
        self.click(LoginpageLocators.LOGOUT_BUTTON)