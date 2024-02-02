import time
from pages.basepage import BasePage
from locators.muignition2.shop_locators import Mui2shoppageLocators


class ShopPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
 
    def item_purchase(self):
        self.click(Mui2shoppageLocators.DIA1100_PURCHASE_BUTTON)                     
        self.switch_to_iframe_index()
        self.click(Mui2shoppageLocators.AGREE_CHECK)
        self.click(Mui2shoppageLocators.PURCHASE_BUTTON)
