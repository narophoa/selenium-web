from selenium import webdriver
from locators.sunclassic.home_locators import SUNCLpageLocators
from pages.sunclassic.homepage import HomePage
from pages.sunclassic.cspage import CSPage
from tests.test_base import BaseTest
import time

class Test_Homepage(BaseTest):

    def test_sunclpageOpen(self): #TID.22 홈페이지 접근 및 PC방 혜택 확인
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert '정식 서비스 오픈 - 썬 클래식' in home_page.get_title()                    
        #is_displayed = home_page.find_element(SUNCLpageLocators.PCBANG_BENEFIT_ON).is_displayed()
        #assert is_displayed is True


    def test_all_page_open(self):
        all_page = HomePage(self.driver)
        all_page.open_notice_page()
        assert '공지사항 - 썬 클래식' in all_page.get_title()
        all_page.open_update_page()
        assert '패치노트 - 썬 클래식' in all_page.get_title()
        all_page.open_gmnote_page()
        assert 'GM노트 - 썬 클래식' in all_page.get_title()
        all_page.open_events_page()
        assert '이벤트 - 썬 클래식' in all_page.get_title()
        all_page.open_introduce_page()
        assert '세계관 : 썬 클래식' in all_page.get_title()
        all_page.open_character_page()
        assert '버서커 : 썬 클래식' in all_page.get_title()
        all_page.open_gameguide_page()
        assert '가이드 : 썬 클래식' in all_page.get_title()
        all_page.open_probability_page()
        assert '확률 정보 - 썬 클래식' in all_page.get_title()
        all_page.open_freeboard_page()
        assert '자유게시판 - 썬 클래식' in all_page.get_title()
        all_page.open_imageboard_page()
        assert '이미지게시판 - 썬 클래식' in all_page.get_title()
        all_page.open_attackboard_page()
        assert '공략 게시판 - 썬 클래식' in all_page.get_title()
        all_page.open_faq_page()
        assert 'FAQ - 썬 클래식' in all_page.get_title()
        # all_page.open_coupon_page()
        # assert '쿠폰등록 - 썬 클래식' in all_page.get_title()        
        all_page.open_policy_page()
        assert '운영정책 - 썬 클래식' in all_page.get_title()        
        all_page.open_download_page()
        assert '게임 다운로드 - 썬 클래식' in all_page.get_title()
        
    
class Test_CSpage(BaseTest):

    def test_write_tickets(self):
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_writepage()
        tickets_page.cs_write()        

    def test_delete_tickets(self):
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_listpage()
        tickets_page.cs_delete()

class Test_topbar_Login(BaseTest):

    def test_topbar_login(self):
        topbar_login = HomePage(self.driver)
        topbar_login.open_home_page()
        topbar_login.click_topbar_login_button()
        topbar_login.login_success()
        assert len(topbar_login.get_cookie('WZ_AUTH')) > 0       

    def test_topbar_logout(self):
        topbar_login = HomePage(self.driver)
        topbar_login.click_topbar_logout_button()        
        assert topbar_login.get_cookie('WZ_AUTH') is None

class Test_site_Login(BaseTest):

    def test_site_login(self):
        site_login = HomePage(self.driver)
        site_login.open_home_page()
        site_login.click_site_login_button()
        site_login.login_success()        
        assert len(site_login.get_cookie('WZ_AUTH')) > 0             

    def test_site_logout(self):
        site_login = HomePage(self.driver)
        site_login.click_site_logout_button()        
        assert site_login.get_cookie('WZ_AUTH') is None
