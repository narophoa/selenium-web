import pytest
from selenium import webdriver
from locators.portal.home_locators import HomepageLocators
from pages.portal.homepage import HomePage
from tests.test_base import BaseTest

class Test_page_load(BaseTest):

    def test_page_load_portal(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert 'Webzen - Games Portal' in home_page.get_title()

    def test_page_load_member(self):
        home_page = HomePage(self.driver)
        home_page.open_member_page()
        assert '로그인 - 웹젠' in home_page.get_title()
