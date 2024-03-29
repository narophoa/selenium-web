import time
from selenium import webdriver
from pages.basepage import BasePage
from pages.portal.loginpage import LoginPage
from locators.muignition2.cs_locators import Mui2CSLocators


class CSPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_cs_writepage(self):
        LoginPage.login_success(self)           
        self.open_url(Mui2CSLocators.PATH_WRITE)     
    
    def open_cs_listpage(self):
        self.open_url(Mui2CSLocators.PATH_LIST)

    def cs_write(self):
        self.send_keys(Mui2CSLocators.PHONE, '92779710')
        self.send_keys(Mui2CSLocators.TITLE, '통상점검 문의테스트입니다.')
        self.send_keys(Mui2CSLocators.CONTENT, '안녕하세요')
        self.click(Mui2CSLocators.AGRPRIVACY)
        self.click(Mui2CSLocators.WRITE)
        time.sleep(2)
        self.alert_accept()
        time.sleep(2)

    def cs_delete(self):
        self.click(Mui2CSLocators.CANCEL)
        time.sleep(2)
        self.alert_accept()    
        time.sleep(2)    
        self.alert_accept()
        time.sleep(2)