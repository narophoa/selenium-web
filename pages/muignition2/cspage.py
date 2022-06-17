import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from locators.muignition2.home_locators import Mui2pageLocators
from pages.basepage import BasePage
from pages.portal.loginpage import LoginPage
from locators.muignition2.cs_locators import Mui2CSLocators
from locators.portal.login_locators import LoginpageLocators

class CSPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_cs_writepage(self):
        LoginPage.login_success(self)
        self.open_url(Mui2CSLocators.PATH_WRITE)
    
    def open_cs_listpage(self):
        LoginPage.login_success(self)
        self.open_url(Mui2CSLocators.PATH_LIST)

    def cs_write(self):
        self.send_keys(Mui2CSLocators.PHONE, '92779710')
        self.send_keys(Mui2CSLocators.TITLE, '통상점검 문의테스트입니다.')
        self.send_keys(Mui2CSLocators.CONTENT, '안녕하세요')
        self.click(Mui2CSLocators.AGRPRIVACY)
        self.click(Mui2CSLocators.WRITE)
        # self.enter()

    def cs_delete(self):
        self.click(Mui2CSLocators.CANCEL)
        # self.alert_accept()
        # time.sleep(3)
        # self.alert_accept()