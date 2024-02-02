from selenium import webdriver
from pages.basepage import BasePage
from locators.sunclassic.home_locators import SUNCLpageLocators
from locators.portal.login_locators import LoginpageLocators
from locators.portal.charge_locators import ChargepageLocators
from config.config import ID, PW

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(SUNCLpageLocators.PATH)

    def open_notice_page(self):
        self.open_url(SUNCLpageLocators.PATH_NOTICE)

    def open_update_page(self):
        self.open_url(SUNCLpageLocators.PATH_UPDATE)

    def open_gmnote_page(self):
        self.open_url(SUNCLpageLocators.PATH_GMNOTE)

    def open_events_page(self):
        self.open_url(SUNCLpageLocators.PATH_EVENTS)
        
    def open_introduce_page(self):
        self.open_url(SUNCLpageLocators.PATH_INTRODUCE)

    def open_character_page(self):
        self.open_url(SUNCLpageLocators.PATH_CHARACTER)
  
    def open_gameguide_page(self):
        self.open_url(SUNCLpageLocators.PATH_GAMEGUIDE)

    def open_probability_page(self):
        self.open_url(SUNCLpageLocators.PATH_PROBABILITY)
    
    def open_freeboard_page(self):
        self.open_url(SUNCLpageLocators.PATH_FREEBOARD)

    def open_imageboard_page(self):
        self.open_url(SUNCLpageLocators.PATH_IMAGEBOARD)

    def open_attackboard_page(self):
        self.open_url(SUNCLpageLocators.PATH_ATTACKBOARD)

    def open_faq_page(self):
        self.open_url(SUNCLpageLocators.PATH_FAQ)
  
    def open_tickets_page(self):
        self.open_url(SUNCLpageLocators.PATH_TICKETS)      
        
    def open_policy_page(self):
        self.open_url(SUNCLpageLocators.PATH_POLICY)
  
    def open_download_page(self):
        self.open_url(SUNCLpageLocators.PATH_DOWNLOAD)

    def open_coupon_page(self):
        self.open_url(SUNCLpageLocators.PATH_COUPON)

    def click_topbar_login_button(self):
        self.click(SUNCLpageLocators.TOPBAR_LOGIN_BUTTON)

    def click_topbar_logout_button(self):
        self.click(SUNCLpageLocators.TOPBAR_LOGOUT_BUTTON)

    def click_site_login_button(self):
        self.click(SUNCLpageLocators.SITE_LOGIN_BUTTON)

    def click_site_logout_button(self):
        self.click(SUNCLpageLocators.SITE_LOGOUT_BUTTON)
    
    def open_usedcash_page(self):
        self.open_url(ChargepageLocators.PATH_USEDCASH)

    def login_success(self): 
        #self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, ID)
        self.send_keys(LoginpageLocators.PASSWORD, PW)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass