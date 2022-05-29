from selenium.webdriver.common.by import By

class Mui2CSLocators:
  PATH_WRITE = "https://muignition2.webzen.co.kr/support/tickets"
  PATH_LIST = "https://muignition2.webzen.co.kr/support/tickets/list"
  PHONE = (By.XPATH, "//*[@class='text text-telephone']")
  TITLE = (By.XPATH, "//*[@id='title']")
  CONTENT = (By.XPATH, "//*[@id='content']")
  AGRPRIVACY = (By.XPATH, "//*/span/label/span")
  WRITE = (By.XPATH, "//*[@class='write']")
  CANCEL = (By.XPATH, "//*[@class='cancel']")