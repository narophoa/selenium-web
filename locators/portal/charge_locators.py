from selenium.webdriver.common.by import By

class ChargepageLocators:
  PATH_CHARGECASH = "https://payment.webzen.co.kr/history/chargeCash"
  PATH_USEDCASH = "https://payment.webzen.co.kr/history/usedcash"
  SELECT_SEARCH_TYPE = (By.XPATH, "//*[@id='selectSearchType']")
  SELECT_MUI2 = (By.XPATH, "//*[@id='selectSearchType']/option[6]")
  SEARCH = (By.XPATH, "//*[@id='contents']/div[1]/form/fieldset/div/div[2]/div/span/a")
  REFUND_BUTTON = (By.XPATH, "//*[@id='contents']/div[3]/form/ul[1]/li[1]/div[3]/span/a") 
  R2_REFUND_TEXT = (By.XPATH, "//*[@id='contents']")
  R2_REFUND_BUTTON = (By.XPATH, ("/html/body/div[1]/div/section/div/form/fieldset/div/a"))
  