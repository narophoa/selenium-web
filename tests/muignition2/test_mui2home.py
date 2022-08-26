import pytest
import time
from selenium import webdriver
from locators.muignition2.home_locators import Mui2pageLocators
from pages.muignition2.homepage import HomePage
from pages.muignition2.cspage import CSPage
from tests.test_base import BaseTest
from pages.portal.loginpage import LoginPage

class Test_Homepage(BaseTest):

    def test_mui2pageOpen(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert '웹게임 No.1 - 뮤 이그니션2' in home_page.get_title()                    
        is_displayed = home_page.find_element(Mui2pageLocators.PCBANG_BENEFIT_ON).is_displayed()
        assert is_displayed is True

    def test_all_page_open(self):
        all_page = HomePage(self.driver)
        all_page.open_notice_page()
        assert '공지사항 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_gmnote_page()
        assert 'GM노트 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_events_page()
        assert '이벤트 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_introduce_page()
        assert '게임소개 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_character_page()
        assert '캐릭터소개 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_beginner_page()
        assert '초보자 가이드 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_gameguide_page()
        assert '게임가이드 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_probability_page()
        assert '확률 정보 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_ranking_page()
        assert '전투력 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_level_page()
        assert '레벨 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_freeboard_page()
        assert '광장게시판 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_joinevent_page()
        assert '이벤트참여게시판 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_faq_page()
        assert 'FAQ - 뮤 이그니션2' in all_page.get_title()
        all_page.open_policy_page()
        assert '운영정책 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_operation_page()
        assert '운영 서비스 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_download_page()
        assert '다운로드 - 뮤 이그니션2' in all_page.get_title()
        all_page.open_shop_page()
        assert 'W샵 - 뮤 이그니션2' in all_page.get_title() 
            
    def test_write_tickets(self):
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_writepage()
        tickets_page.cs_write()    

    def test_delete_tickets(self):
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_listpage()
        tickets_page.cs_delete()

    def test_topbar_login_logout(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_topbar_login_button()
        home_page.login_success()
        assert len(home_page.get_cookie('WZ_AUTH')) > 0
        home_page.click_topbar_logout_button()
        assert home_page.get_cookie('WZ_AUTH') is None

    def test_site_login_logout(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_site_login_button
        home_page.login_success()
        assert len(home_page.get_cookie('WZ_AUTH')) > 0
        home_page.click_site_logout_button()
        assert home_page.get_cookie('WZ_AUTH') is None

        