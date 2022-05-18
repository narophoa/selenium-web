from selenium import webdriver
from pages.basepage import BasePage
from locators.portal.home_locators import HomepageLocators

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(HomepageLocators.PATH)

    def click_login_button(self):
        self.click(HomepageLocators.LOGIN)