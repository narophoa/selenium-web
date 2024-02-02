import time
from selenium import webdriver
from pages.basepage import BasePage
from pages.portal.loginpage import LoginPage
from locators.shotonline.cs_locators import ShotCSLocators

class CSPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_cs_writepage(self):
        LoginPage.login_success(self)           
        self.open_url(ShotCSLocators.PATH_WRITE)     
    
    def open_cs_listpage(self):
        self.open_url(ShotCSLocators.PATH_LIST)

    def cs_write(self):
        self.send_keys(ShotCSLocators.PHONE, '92779710')
        self.send_keys(ShotCSLocators.TITLE, '통상점검 문의테스트입니다.')
        self.send_keys(ShotCSLocators.CONTENT, '안녕하세요')
        self.click(ShotCSLocators.AGRPRIVACY)
        self.click(ShotCSLocators.WRITE)
        time.sleep(2)
        self.alert_accept()
        time.sleep(2)

    def cs_delete(self):
        self.click(ShotCSLocators.CANCEL)
        time.sleep(2)
        self.alert_accept()    
        time.sleep(2)    
        self.alert_accept()
        time.sleep(2)