from selenium.webdriver.common.by import By

class Mui2CSLocators:
  PATH = "https://muignition2.webzen.co.kr/support/tickets"
  PHONE = (By.XPATH, "//*[@class='text text-telephone']")
  TITLE = (By.XPATH, "//*[@id='title']")
  CONTENT = (By.XPATH, "//*[@id='content']")
  AGRPRIVACY = (By.XPATH, "//*/span/label/span")
  WRITE = (By.XPATH, "//*[@class='write']")