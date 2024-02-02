from selenium import webdriver
from pages.basepage import BasePage
from locators.shotonline.home_locators import ShotpageLocators
from locators.portal.login_locators import LoginpageLocators
from locators.portal.charge_locators import ChargepageLocators
from config.config import SHOTID, SHOTPW

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_url(ShotpageLocators.PATH)

    def open_notices(self):
        self.open_url(ShotpageLocators.PATH_NOTICES)

    def open_patchnote(self):
        self.open_url(ShotpageLocators.PATH_PATCHNOTE)

    def open_updates(self):
        self.open_url(ShotpageLocators.PATH_UPDATES)
   
    def open_event(self):
        self.open_url(ShotpageLocators.PATH_EVENT)
    
    def open_bodo(self):
        self.open_url(ShotpageLocators.PATH_BODO)    

    def open_game_info(self):
        self.open_url(ShotpageLocators.PATH_GAME_INFO)

    def open_game_guide(self):
        self.open_url(ShotpageLocators.PATH_GAME_GUIDE)

    def open_course_ranking(self):
        self.open_url(ShotpageLocators.PATH_COURSE_RANKING)

    def open_world_ranking(self):
        self.open_url(ShotpageLocators.PATH_WORLD_RANKING)

    def open_personal_ranking(self):
        self.open_url(ShotpageLocators.PATH_PERSONAL_RAKING)

    def open_channel_ranking(self):
        self.open_url(ShotpageLocators.PATH_CHANNEL_RANKING)
    
    def open_guild_ranking(self):
        self.open_url(ShotpageLocators.PATH_GUILD_RANKING)

    def open_guild_sketch(self):
        self.open_url(ShotpageLocators.PATH_GUILD_SKETCH)

    def open_story(self):
        self.open_url(ShotpageLocators.PATH_STORY)

    def open_discussion(self):
        self.open_url(ShotpageLocators.PATH_DISCUSSION)

    def open_study(self):
        self.open_url(ShotpageLocators.PATH_STUDY)

    def open_screenshot(self):
        self.open_url(ShotpageLocators.PATH_SCREENSHOT)

    def open_survey(self):
        self.open_url(ShotpageLocators.PATH_SURVEY)

    def open_shop(self):
        self.open_url(ShotpageLocators.PATH_SHOP)

    def open_prob(self):
        self.open_url(ShotpageLocators.PATH_PROB)

    def open_faq(self):
        self.open_url(ShotpageLocators.PATH_FAQ)

    def open_cs(self):
        self.open_url(ShotpageLocators.PATH_CS)

    def open_download(self):
        self.open_url(ShotpageLocators.PATH_DOWNLOAD)

    def open_policy(self):
        self.open_url(ShotpageLocators.PATH_POLICY)

    def login_success(self): 
        self.open_url(LoginpageLocators.PATH)
        self.send_keys(LoginpageLocators.ID, SHOTID)
        self.send_keys(LoginpageLocators.PASSWORD, SHOTPW)
        self.click(LoginpageLocators.LOGIN_BUTTON)     
        if self.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            self.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            pass