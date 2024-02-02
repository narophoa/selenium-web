from selenium import webdriver
from locators.r2.home_locators import R2pageLocators
from locators.r2.shop_locators import R2shoppageLocators
from locators.portal.charge_locators import ChargepageLocators
from pages.portal.chargepage import ChargePage
from pages.r2.homepage import HomePage
from pages.r2.cspage import CSPage
from pages.r2.shoppage import ShopPage
from tests.test_base import BaseTest
import time

class Test_Homepage(BaseTest):

    def test_r2pageOpen(self): #TID.12 홈페이지 접근 및 PC방 혜택 확인
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert '홈 - R2' in home_page.get_title()                    
        # is_displayed = home_page.find_element(R2pageLocators.PCBANG_BENEFIT_ON).is_displayed()
        # assert is_displayed is True

    def test_all_page_open(self): #TID.13 전체 페이지 접근 확인
        all_page = HomePage(self.driver)
        all_page.open_notices()
        assert '공지사항 - R2' in all_page.get_title()
        all_page.open_updates()
        assert '업데이트 - R2' in all_page.get_title()
        all_page.open_events()
        assert '이벤트 - R2' in all_page.get_title()
        all_page.open_history()
        assert '히스토리 - R2' in all_page.get_title()
        all_page.open_pcbang_go()
        assert 'R2가 PC방에서 쏜다! - R2' in all_page.get_title()
        all_page.open_game_features()
        assert '게임 특징 - R2' in all_page.get_title()
        all_page.open_server_guide()
        assert '서버가이드 - R2' in all_page.get_title()
        all_page.open_boot_camp()
        assert '신병훈련소 - R2' in all_page.get_title()
        all_page.open_game_guide()
        assert '세부가이드 - R2' in all_page.get_title()
        all_page.open_supply()
        assert 'R2' in all_page.get_title()
        all_page.open_guild_war()
        assert '통합 길드전 - R2' in all_page.get_title()
        all_page.open_seige()
        assert '공성 & 스팟 - R2' in all_page.get_title()
        all_page.open_ranking()
        assert '랭킹 - R2' in all_page.get_title()
        all_page.open_tournament7()
        assert 'R2Match 2022 - R2' in all_page.get_title()
        all_page.open_free_board()
        assert '자유게시판 - R2' in all_page.get_title()
        all_page.open_image_board()
        assert '이미지게시판 - R2' in all_page.get_title()
        all_page.open_tip_board()
        assert 'TIP게시판 - R2' in all_page.get_title()
        all_page.open_gm_note()
        assert 'GM노트 - R2' in all_page.get_title()
        all_page.open_game_download()
        assert '게임다운로드 - R2' in all_page.get_title()
        all_page.open_media()
        assert '갤러리 - R2' in all_page.get_title()
        all_page.open_r2shop()
        assert 'Webzen - WEB SHOP' in all_page.get_title()

class Test_CSpage(BaseTest):

    def test_write_tickets(self): #TID.14 문의 접수 CS 등록 기능 확인
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_writepage()
        tickets_page.cs_write()        

    def test_delete_tickets(self): #TID.15 문의 접수 CS 등록 기능 확인
        tickets_page = CSPage(self.driver)
        tickets_page.open_cs_listpage()
        tickets_page.cs_delete()

class Test_topbar_Login(BaseTest):

    def test_topbar_login(self): #TID.16 Topbar 로그인 기능 확인
        topbar_login = HomePage(self.driver)
        topbar_login.open_home_page()
        topbar_login.click_topbar_login_button()
        topbar_login.login_success2()
        time.sleep(1)
        assert len(topbar_login.get_cookie('WZ_AUTH')) > 0       

    def test_topbar_logout(self): #TID.17 Topbar 로그아웃 기능 확인
        topbar_login = HomePage(self.driver)
        topbar_login.click_topbar_logout_button()
        time.sleep(1)
        assert topbar_login.get_cookie('WZ_AUTH') is None        

class Test_site_Login(BaseTest):

    def test_site_login(self): #TID.18 Site 로그인 기능 확인
        site_login = HomePage(self.driver)
        site_login.open_home_page()
        site_login.click_site_login_button()
        site_login.login_success2()
        time.sleep(1)        
        assert len(site_login.get_cookie('WZ_AUTH')) > 0             

    def test_site_logout(self): #TID.19 Site 로그아웃 기능 확인
        site_login = HomePage(self.driver)
        site_login.click_site_logout_button()
        time.sleep(1)      
        assert site_login.get_cookie('WZ_AUTH') is None

class Test_R2Shop(BaseTest):

    def test_r2shoppageOpen(self): #TID.20 R2shop 접근 확인
        shop_page = HomePage(self.driver)        
        shop_page.open_r2shop()        
        shop_page.click_shop_topbar_login_button()
        shop_page.login_success2()                
        assert 'Webzen - WEB SHOP' in shop_page.get_title()

    def test_r2shop_purchage(self): #TID.21 상품 구매 기능 확인
        shop_page = ShopPage(self.driver)
        shop_page.item_purchase()
    

    #로딩 지연으로 방법 찾는중
    # def test_r2shop_refund(self):
    #     shop_page = ChargePage(self.driver)                          
    #     shop_page.open_usedcash_page()                
    #     shop_page.select_search_type('R2')
    #     shop_page.r2_refund_itme()