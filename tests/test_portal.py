import unittest
from selenium import webdriver
from locators.locators import HomepageLocators

class TestPortal():

    def test_page_load_portal(self):
        driver = webdriver.Chrome()
        driver.get(HomepageLocators.PORTAL_PATH)
        title = driver.title
        assert 'Webzen - Games Portal' in title

    def test_page_load_member(self):
        driver = webdriver.Chrome()
        driver.get(HomepageLocators.MEMBER_PATH)
        title = driver.title
        assert '로그인 - 웹젠' in title
