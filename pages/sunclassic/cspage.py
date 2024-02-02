import time
from selenium import webdriver
from pages.basepage import BasePage
from pages.portal.loginpage import LoginPage
from locators.sunclassic.cs_locators import SUNCLCSLocators


class CSPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_cs_writepage(self):
        LoginPage.login_success(self)           
        self.open_url(SUNCLCSLocators.PATH_WRITE)     
    
    def open_cs_listpage(self):
        self.open_url(SUNCLCSLocators.PATH_LIST)

    def cs_write(self):
        self.send_keys(SUNCLCSLocators.PHONE, '92779710')
        self.send_keys(SUNCLCSLocators.TITLE, '통상점검 문의테스트입니다.')
        self.send_keys(SUNCLCSLocators.CONTENT, '안녕하세요')
        self.click(SUNCLCSLocators.AGRPRIVACY)
        self.click(SUNCLCSLocators.AGRSMS)
        self.click(SUNCLCSLocators.WRITE)
        time.sleep(2)
        self.alert_accept()
        time.sleep(2)

    def cs_delete(self):
        self.click(SUNCLCSLocators.CANCEL)
        time.sleep(2)
        self.alert_accept()    
        time.sleep(2)    
        self.alert_accept()
        time.sleep(2)