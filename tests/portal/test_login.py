from ast import Pass
import pytest
import time
from selenium import webdriver
from locators.portal.home_locators import HomepageLocators
from locators.portal.login_locators import LoginpageLocators
from pages.muignition2.homepage import HomePage
from pages.portal.loginpage import LoginPage
from tests.test_base import BaseTest

class Test_login(BaseTest):

    #Login page open
    def test_loginpageOpen(self): 
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        assert "로그인 - 웹젠" in login_page.get_title()

    #Login
    def test_login_success(self): 
        login_page = LoginPage(self.driver)        
        login_page.login_success()
        assert len(login_page.get_cookie('WZ_AUTH')) > 0

    #Logout
    def test_logout(self):        
        logout_page = LoginPage(self.driver)
        logout_page.logout() 
        assert logout_page.get_cookie('WZ_AUTH') is None
