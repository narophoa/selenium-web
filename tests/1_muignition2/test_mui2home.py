from selenium import webdriver
from locators.muignition2.home_locators import Mui2pageLocators
from locators.muignition2.shop_locators import Mui2shoppageLocators
from locators.portal.charge_locators import ChargepageLocators
from pages.portal.chargepage import ChargePage
from pages.muignition2.homepage import HomePage
from pages.muignition2.cspage import CSPage
from pages.muignition2.shoppage import ShopPage
from pages.muignition2.channelpage import ChannelPage
from tests.test_base import BaseTest
import time

class Test_Homepage(BaseTest):

    def test_mui2pageOpen(self):# TID.1 홈페이지 접근 및 PC방 혜택 확인
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert '웹게임 No.1 - 뮤 이그니션2' in home_page.get_title()                    
        is_displayed = home_page.find_element(Mui2pageLocators.PCBANG_BENEFIT_ON).is_displayed()
        assert is_displayed is True

    def test_all_page_open(self):# TID.2 전체 페이지 접근 확인
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
    
class Test_CSpage(BaseTest):

    def test_write_tickets(self):# TID.3 문의 접수 CS 등록 기능 확인
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_writepage()
        tickets_page.cs_write()        

    def test_delete_tickets(self):# TID.4 문의 접수 CS 삭제 기능 확인
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_listpage()
        tickets_page.cs_delete()

class Test_topbar_Login(BaseTest):

    def test_topbar_login(self):# TID.5 Topbar 로그인 기능 확인
        topbar_login = HomePage(self.driver)
        topbar_login.open_home_page()
        topbar_login.click_topbar_login_button()
        topbar_login.login_success()
        assert len(topbar_login.get_cookie('WZ_AUTH')) > 0       

    def test_topbar_logout(self):# TID.6 Topbar 로그아웃 기능 확인
        topbar_login = HomePage(self.driver)
        topbar_login.click_topbar_logout_button()        
        assert topbar_login.get_cookie('WZ_AUTH') is None

class Test_site_Login(BaseTest):

    def test_site_login(self):# TID.7 Site 로그인 기능 확인
        site_login = HomePage(self.driver)
        site_login.open_home_page()
        site_login.click_site_login_button()
        site_login.login_success()        
        assert len(site_login.get_cookie('WZ_AUTH')) > 0             

    def test_site_logout(self):# TID.8 Site 로그아웃 기능 확인
        site_login = HomePage(self.driver)
        site_login.click_site_logout_button()        
        assert site_login.get_cookie('WZ_AUTH') is None

class Test_MUI2Shop(BaseTest):

    def test_mui2shoppageOpen(self):# TID.9 W샵 접근 확인(로그인 상태)
        shop_page = HomePage(self.driver)        
        shop_page.open_shop_page()        
        shop_page.click_topbar_login_button()
        shop_page.login_success()                
        assert 'W샵 - 뮤 이그니션2' in shop_page.get_title()

    def test_mui2shop_purchage(self):# TID.10 다이아 구매 기능 확인
        shop_page = ShopPage(self.driver)
        shop_page.item_purchase()
    
    def test_mui2shop_refund(self):# TID.11 구매 상품 구매 철회 기능 확인
        shop_page = ChargePage(self.driver)                          
        shop_page.open_usedcash_page()        
        #shop_page.login_success()     #테스트용
        shop_page.select_search_type('뮤 이그니션2')
        shop_page.mui2_refund_itme()

# 네이버 자동 입력 방지 우회 문제로 보류중
# class Test_MUI2Channel(BaseTest):

#     def test_mui2_naver_login(self):
#         channel_page = ChannelPage(self.driver)        
#         channel_page.login_success()
#         time.sleep(3)
