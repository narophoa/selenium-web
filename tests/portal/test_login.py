from ast import Pass
import pytest
import time
from selenium import webdriver
from locators.portal.home_locators import HomepageLocators
from locators.portal.login_locators import LoginpageLocators
from pages.portal.homepage import HomePage
from pages.portal.loginpage import LoginPage
from tests.test_base import BaseTest

class Test_login(BaseTest):

    #Login page open test
    def test_loginpageOpen(self): 
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        assert "로그인 - 웹젠" in login_page.get_title()

    #Login test
    def test_login(self): 
        login_page = LoginPage(self.driver)        
        login_page.send_keys(LoginpageLocators.ID, "wtwt")
        login_page.send_keys(LoginpageLocators.PASSWORD, "webzen@1")
        login_page.click(LoginpageLocators.LOGIN_BUTTON)     
        assert len(login_page.get_cookie('WZ_AUTH')) > 0

        if login_page.find_element(LoginpageLocators.CHANGE_PASSWORD) :
            login_page.click(LoginpageLocators.CHANGE_PASSWORD)
        else :
            Pass

    #Logout test
    def test_logout(self):        
        logout_page = LoginPage(self.driver)
        logout_page.open_url(HomepageLocators.PATH)
        logout_page.click(HomepageLocators.LOGOUT)        
        assert logout_page.get_cookie('WZ_AUTH') is None
