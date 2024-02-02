from selenium import webdriver
from locators.shotonline.home_locators import ShotpageLocators
from locators.shotonline.shop_locators import ShotshoppageLocators
from pages.shotonline.homepage import HomePage
from pages.shotonline.loginpage import LoginPage
from pages.shotonline.cspage import CSPage
from pages.shotonline.shoppage import ShopPage
from tests.test_base import BaseTest
import time

class Test_Homepage(BaseTest):

    def test_all_page_open(self):
        all_page = HomePage(self.driver)
        all_page.open_notices()
        assert '전체 - 공지사항 - 샷온라인' in all_page.get_title()

        all_page.open_patchnote()
        assert '전체 - 샷온라인' in all_page.get_title()

        all_page.open_updates()
        assert '업데이트 - 샷온라인' in all_page.get_title()

        all_page.open_event()
        assert '진행중인 이벤트 - 이벤트 - 샷온라인' in all_page.get_title()

        all_page.open_bodo()
        assert '보도자료 - 샷온라인' in all_page.get_title()

        all_page.open_game_info()
        assert '게임소개 - 샷온라인' in all_page.get_title()

        all_page.open_game_guide()
        assert '게임 가이드 - 샷온라인' in all_page.get_title()

        all_page.open_course_ranking()
        assert '월별랭킹 - 코스 레코드 - 샷온라인' in all_page.get_title()

        all_page.open_world_ranking()
        assert '월드 랭킹 투어 - 샷온라인' in all_page.get_title()

        all_page.open_personal_ranking()
        assert '개인 매치 - 샷온라인' in all_page.get_title()

        all_page.open_channel_ranking()
        assert '채널 대회 - 샷온라인' in all_page.get_title()

        all_page.open_guild_ranking()
        assert '길드 랭킹 - 샷온라인' in all_page.get_title()

        all_page.open_guild_sketch()
        assert '길드 리포트 - 샷온라인' in all_page.get_title()

        all_page.open_story()
        assert '이야기 - 샷온 이야기 - 샷온라인' in all_page.get_title()

        all_page.open_discussion()
        assert '토론 광장 - 샷온라인' in all_page.get_title()

        all_page.open_study()
        assert '샷온 공부방 - 샷온라인' in all_page.get_title()

        all_page.open_screenshot()
        assert '스크린샷 - 샷온라인' in all_page.get_title()

        all_page.open_survey()
        assert '샷온 POLL - 샷온라인' in all_page.get_title()

        all_page.open_shop()
        assert '샷온라인' in all_page.get_title()

        all_page.open_prob()
        assert '확률 정보 - 샷온라인' in all_page.get_title()

        all_page.open_faq()
        assert 'FAQ - 샷온라인' in all_page.get_title()

        all_page.open_cs()
        assert '1:1 문의 - 샷온라인' in all_page.get_title()

        all_page.open_download()
        assert '다운로드 - 샷온라인' in all_page.get_title()

        all_page.open_policy()
        assert '운영정책 - 샷온라인' in all_page.get_title()

class Test_Login(BaseTest):

    def test_login(self):
        login = LoginPage(self.driver)
        login.login_success()        
        time.sleep(1)
        assert len(login.get_cookie('SHOT_AUTH')) > 0              

class Test_Logout(BaseTest):

    def test_logout(self):
        logout = LoginPage(self.driver)
        logout.logout()
        time.sleep(1)
        assert logout.get_cookie('SHOT_AUTH') is None        









# class Test_CSpage(BaseTest):

#     def test_write_tickets(self):
#         tickets_page = CSPage(self.driver)
#         tickets_page.open_cs_writepage()
#         tickets_page.cs_write()        

#     def test_delete_tickets(self):
#         tickets_page = CSPage(self.driver)
#         tickets_page.open_cs_listpage()
#         tickets_page.cs_delete()

# class Test_Login(BaseTest):

#     def test_topbar_login(self):
#         topbar_login = HomePage(self.driver)
#         topbar_login.open_home_page()
#         topbar_login.click_topbar_login_button()
#         topbar_login.login_success2()
#         time.sleep(1)
#         assert len(topbar_login.get_cookie('WZ_AUTH')) > 0       

#     def test_topbar_logout(self):
#         topbar_login = HomePage(self.driver)
#         topbar_login.click_topbar_logout_button()
#         time.sleep(1)
#         assert topbar_login.get_cookie('WZ_AUTH') is None        

# class Test_site_Login(BaseTest):

#     def test_site_login(self):
#         site_login = HomePage(self.driver)
#         site_login.open_home_page()
#         site_login.click_site_login_button()
#         site_login.login_success2()
#         time.sleep(1)        
#         assert len(site_login.get_cookie('WZ_AUTH')) > 0             

#     def test_site_logout(self):
#         site_login = HomePage(self.driver)
#         site_login.click_site_logout_button()
#         time.sleep(1)      
#         assert site_login.get_cookie('WZ_AUTH') is None

# class Test_R2Shop(BaseTest):

#     def test_r2shoppageOpen(self):
#         shop_page = HomePage(self.driver)        
#         shop_page.open_r2shop()        
#         shop_page.click_shop_topbar_login_button()
#         shop_page.login_success2()                
#         assert 'Webzen - WEB SHOP' in shop_page.get_title()

#     def test_r2shop_purchage(self):
#         shop_page = ShopPage(self.driver)
#         shop_page.item_purchase()
    

##     로딩 지연으로 방법 찾는중
#     def test_r2shop_refund(self):
#         shop_page = ChargePage(self.driver)                          
#         shop_page.open_usedcash_page()                
#         shop_page.select_search_type('R2')
#         shop_page.r2_refund_itme()