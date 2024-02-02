from selenium import webdriver
from pages.basepage import BasePage
from locators.r2.home_locators import R2pageLocators
from locators.portal.login_locators import LoginpageLocators
from locators.portal.charge_locators import ChargepageLocators
from config.config import ID2, PW2

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(R2pageLocators.PATH)

    def open_notices(self):
        self.open_url(R2pageLocators.PATH_NOTICES)

    def open_updates(self):
        self.open_url(R2pageLocators.PATH_UPDATES)
   
    def open_events(self):
        self.open_url(R2pageLocators.PATH_EVENTS)
    
    def open_history(self):
        self.open_url(R2pageLocators.PATH_HISTORY)    

    def open_pcbang_go(self):
        self.open_url(R2pageLocators.PATH_PCBANG_GO)

    def open_game_features(self):
        self.open_url(R2pageLocators.PATH_GAME_FEATURES)

    def open_server_guide(self):
        self.open_url(R2pageLocators.PATH_SERVER_GUIDE)

    def open_boot_camp(self):
        self.open_url(R2pageLocators.PATH_BOOT_CAMP)

    def open_game_guide(self):
        self.open_url(R2pageLocators.PATH_GAME_GUIDE)

    def open_supply(self):
        self.open_url(R2pageLocators.PATH_SUPPLY)

    def open_guild_war(self):
        self.open_url(R2pageLocators.PATH_GUILD_WAR)

    def open_seige(self):
        self.open_url(R2pageLocators.PATH_SEIGE)

    def open_ranking(self):
        self.open_url(R2pageLocators.PATH_RANKING)

    def open_tournament7(self):
        self.open_url(R2pageLocators.PATH_TOURNAMENT7)

    def open_free_board(self):
        self.open_url(R2pageLocators.PATH_FREE_BOARD)

    def open_image_board(self):
        self.open_url(R2pageLocators.PATH_IMAGE_BOARD)

    def open_tip_board(self):
        self.open_url(R2pageLocators.PATH_TIP_BOARD)

    def open_gm_note(self):
        self.open_url(R2pageLocators.PATH_GM_NOTE)

    def open_game_download(self):
        self.open_url(R2pageLocators.PATH_GAME_DOWNLOAD)

    def open_media(self):
        self.open_url(R2pageLocators.PATH_MEDIA)

    def open_r2shop(self):
        self.open_url(R2pageLocators.PATH_R2SHOP)

    def open_r2myshop(self):
        self.open_url(R2pageLocators.PATH_R2MYSHOP)

    def open_mycash(self):
        self.open_url(R2pageLocators.PATH_MYCASH)

    def open_faq(self):
        self.open_url(R2pageLocators.PATH_FAQ)

    def open_tickets(self):
        self.open_url(R2pageLocators.PATH_TICKETS)

    def open_security_card(self):
        self.open_url(R2pageLocators.PATH_SECURITY_CARD)

    def open_policy(self):
        self.open_url(R2pageLocators.PATH_POLICY)

    def click_topbar_login_button(self):
        self.click(R2pageLocators.TOPBAR_LOGIN_BUTTON)

    def click_topbar_logout_button(self):
        self.click(R2pageLocators.TOPBAR_LOGOUT_BUTTON)

    def click_site_login_button(self):
        self.click(R2pageLocators.SITE_LOGIN_BUTTON)

    def click_site_logout_button(self):
        self.click(R2pageLocators.SITE_LOGOUT_BUTTON)

    def click_shop_topbar_login_button(self):
        self.click(R2pageLocators.SHOP_TOPBAR_LOGIN_BUTTON)
    
    def open_usedcash_page(self):
        self.open_url(ChargepageLocators.PATH_USEDCASH)

    def login_success2(self): 
        #self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, ID2)
        self.send_keys(LoginpageLocators.PASSWORD, PW2)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass