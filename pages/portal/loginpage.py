from selenium import webdriver
from pages.basepage import BasePage
from locators.portal.login_locators import LoginpageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(LoginpageLocators.PATH)