import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pages.basepage import BasePage
from locators.portal.charge_locators import ChargepageLocators
from locators.portal.login_locators import LoginpageLocators
from config.config import ID, PW, WRONG_PW
from selenium.webdriver.common.by import By

class ChargePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def login_success(self):  
        self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, ID)
        self.send_keys(LoginpageLocators.PASSWORD, PW)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass

    def open_usedcash_page(self):
        self.open_url(ChargepageLocators.PATH_USEDCASH)    

    def select_search_type(self, game):        
        select = Select(self.driver.find_element(By.XPATH, "//*[@id='selectSearchType']"))
        select.select_by_visible_text(game)        
        self.click(ChargepageLocators.SEARCH)

    def mui2_refund_itme(self):
        self.click(ChargepageLocators.REFUND_BUTTON)
        time.sleep(2)
        self.alert_accept()    
        time.sleep(2)    
        self.alert_accept()
        time.sleep(2)

    def r2_refund_itme(self):
        self.click(ChargepageLocators.REFUND_BUTTON)   
        self.switch_to_window_1()            
        self.send_keys(ChargepageLocators.R2_REFUND_TEXT, '구매철회 테스트입니다.')
        self.click(ChargepageLocators.R2_REFUND_BUTTON)        
        time.sleep(2)
        self.alert_accept()
        time.sleep(2)
        # self.alert_accept()
        # time.sleep(2)