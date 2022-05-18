import pytest
import time
from selenium import webdriver
from locators.portal.home_locators import HomepageLocators
from locators.portal.login_locators import LoginpageLocators
from pages.portal.homepage import HomePage
from pages.portal.loginpage import LoginPage
from tests.test_base import BaseTest

class Test_login(BaseTest):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        assert '로그인 - 웹젠' in login_page.get_title()
        
        login_page.send_keys(LoginpageLocators.ID, 'wewe')
        login_page.send_keys(LoginpageLocators.PASSWORD, 'webzen@1')
        login_page.click(LoginpageLocators.LOGIN_BUTTON)
        assert len(login_page.get_cookies()) > 0

        time.sleep(3)

class Test_logout(BaseTest):

    def test_logout(self):
        Test_login.test_login(self)
        logout_page = LoginPage(self.driver)
        logout_page.open_url(HomepageLocators.PATH)
        logout_page.click(HomepageLocators.LOGOUT)

        time.sleep(3)

        assert logout_page.get_cookies() is None
