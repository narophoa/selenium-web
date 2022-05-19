import pytest
import time
from selenium import webdriver
from locators.muignition2.home_locators import HomepageLocators
from locators.portal.login_locators import LoginpageLocators
from pages.muignition2.homepage import HomePage
from tests.test_base import BaseTest

class Test_page_load(BaseTest):

    def test_mui2pageOpen(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert '웹게임 No.1 - 뮤 이그니션2' in home_page.get_title()
    
    def test_tickets(self):
        tickets_page = HomePage(self.driver)
        tickets_page.move_cs()
