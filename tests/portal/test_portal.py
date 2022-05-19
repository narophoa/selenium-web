import pytest
import time
from selenium import webdriver
from locators.portal.home_locators import HomepageLocators
from locators.portal.login_locators import LoginpageLocators
from pages.portal.homepage import HomePage
from tests.test_base import BaseTest

class Test_page_load(BaseTest):

    def test_portalpageOpen(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert 'Webzen - Games Portal' in home_page.get_title()