from selenium import webdriver
from pages.basepage import BasePage
from locators.muignition2.channel_locators import Mui2ChannelLocators
from selenium.webdriver.common.keys import Keys
from config.config import NAVER_ID, NAVER_PW
import pyperclip
import time

class ChannelPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(Mui2ChannelLocators.PATH_NAVER)

    def login_success(self): 
        self.open_url(Mui2ChannelLocators.PATH_NAVER)
        self.click(Mui2ChannelLocators.NAVER_LOGIN_BUTTON)        
        elem_id = self.driver.find_element_by_id('id')
        elem_id.click()
        pyperclip.copy(NAVER_ID)        
        elem_id.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        elem_pw = self.driver.find_element_by_id('pw')
        elem_pw.click()
        pyperclip.copy(NAVER_PW)        
        elem_pw.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        self.click(Mui2ChannelLocators.NAVER_LOGIN_SUBMIT)
