from selenium.webdriver.common.by import By

class Mui2shoppageLocators:
  PATH_SHOP = "https://muignition2.webzen.co.kr/shop"
  CASH_CHARGE_BUTTON = (By.XPATH, "//*[@id='contents']/section/header/div/div/article/fieldset/ul/li[1]/a")
  DIA1100_PURCHASE_BUTTON = (By.XPATH, "//*[@id='contents']/section/section/section/ul/li[10]/div/div[2]/a[1]")
  AGREE_CHECK = (By.XPATH, "//*[@id='chk_agree']")  
  PURCHASE_BUTTON = (By.XPATH, "//*[@id='btnPurchase']")
  POPUP_CLOSE_BUTTON = (By.XPATH, "//*[@id='contents']/section/div/a")
