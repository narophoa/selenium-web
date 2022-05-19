from selenium import webdriver
from pages.basepage import BasePage
from locators.muignition2.home_locators import HomepageLocators

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(HomepageLocators.PATH)

    def move_cs(self):
        self.click(HomepageLocators.SUPPORT)
        self.click(HomepageLocators.TICKETS)
