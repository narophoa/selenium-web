import time
from pages.basepage import BasePage
from locators.r2.shop_locators import R2shoppageLocators


class ShopPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
 
    def item_purchase(self):
        self.click(R2shoppageLocators.OPENREBOOT)              
        self.click(R2shoppageLocators.ITME_ORDER_ASC)
        self.click(R2shoppageLocators.ITME_PURCHASE_BUTTON)
        time.sleep(1)
        self.switch_to_iframe_index()
        self.click(R2shoppageLocators.AGREE_CHECK)
        time.sleep(1)
        self.click(R2shoppageLocators.PURCHASE_BUTTON)       
        time.sleep(1)
        self.alert_accept()