from selenium.webdriver.common.by import By

class R2shoppageLocators:
  PATH_SHOP = "https://r2shop.webzen.co.kr/Main"
  CASH_CHARGE_BUTTON = (By.XPATH, "//*[@id='user_panel_wrp']/div/div/article/dl/dd/div[2]/a[1]")
  OPENREBOOT = (By.XPATH, "//*[@id='body_conts_wrap']/div/nav/ul/li[8]/a/dl/dd")  
  ITME_ORDER_ASC = (By.XPATH, "//*[@id='root']/div/div[4]/div[1]/ul/li[3]/a")
  ITME_PURCHASE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[4]/div[2]/ul/li[2]/div/ul/li[2]/div/button[2]") #2023-12-29 신년감사팩 추가로 Locators 변경
  AGREE_CHECK = (By.XPATH, "//*[@id='webshop_popWrp']/article/div[1]/div[7]/p/label")  
  PURCHASE_BUTTON = (By.XPATH, "//*[@id='btnPurchase']")
  POPUP_CLOSE_BUTTON = (By.XPATH, "//*[@id='webshop_popWrp']/h1/span[2]/a/img")