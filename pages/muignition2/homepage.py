from selenium import webdriver
from pages.basepage import BasePage
from locators.muignition2.home_locators import Mui2pageLocators

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(Mui2pageLocators.PATH)

    def open_notice_page(self):
        self.open_url(Mui2pageLocators.PATH_NOTICE)

    def open_gmnote_page(self):
        self.open_url(Mui2pageLocators.PATH_GMNOTE)

    def open_events_page(self):
        self.open_url(Mui2pageLocators.PATH_EVENTS)
        
    def open_introduce_page(self):
        self.open_url(Mui2pageLocators.PATH_INTRODUCE)

    def open_character_page(self):
        self.open_url(Mui2pageLocators.PATH_CHARACTER)
  
    def open_beginner_page(self):
        self.open_url(Mui2pageLocators.PATH_BEGINNER)

    def open_gameguide_page(self):
        self.open_url(Mui2pageLocators.PATH_GAMEGUIDE)

    def open_probability_page(self):
        self.open_url(Mui2pageLocators.PATH_PROBABILITY)
  
    def open_ranking_page(self):
        self.open_url(Mui2pageLocators.PATH_RANKING)       
        
    def open_level_page(self):
        self.open_url(Mui2pageLocators.PATH_LEVEL)
  
    def open_freeboard_page(self):
        self.open_url(Mui2pageLocators.PATH_FREEBOARD)

    def open_joinevent_page(self):
        self.open_url(Mui2pageLocators.PATH_JOINEVENT)

    def open_faq_page(self):
        self.open_url(Mui2pageLocators.PATH_FAQ)
  
    def open_tickets_page(self):
        self.open_url(Mui2pageLocators.PATH_TICKETS)      
        
    def open_policy_page(self):
        self.open_url(Mui2pageLocators.PATH_POLICY)
  
    def open_operation_page(self):
        self.open_url(Mui2pageLocators.PATH_OPERATION)

    def open_download_page(self):
        self.open_url(Mui2pageLocators.PATH_DOWNLOAD)

    def open_shop_page(self):
        self.open_url(Mui2pageLocators.PATH_SHOP)
  
    def open_storage_page(self):
        self.open_url(Mui2pageLocators.PATH_STORAGE)     

    def click_login_button(self):
        self.click(Mui2pageLocators.TOPBAR_LOGIN_BUTTON)

    def click_logout_button(self):
        self.click(Mui2pageLocators.TOPBAR_LOGOUT_BUTTON)