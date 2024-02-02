import time
from pages.basepage import BasePage
from locators.shotonline.shop_locators import ShotshoppageLocators


class ShopPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
 
    def item_purchase(self):
        self.click(ShotshoppageLocators.OPENREBOOT)              
        self.click(ShotshoppageLocators.ITME_ORDER_ASC)
        self.click(ShotshoppageLocators.ITME_PURCHASE_BUTTON)
        time.sleep(1)
        self.switch_to_iframe_index()
        self.click(ShotshoppageLocators.AGREE_CHECK)
        time.sleep(1)
        self.click(ShotshoppageLocators.PURCHASE_BUTTON)       
        time.sleep(1)
        self.alert_accept()