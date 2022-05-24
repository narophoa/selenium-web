from selenium.webdriver.common.by import By

class Mui2pageLocators:
  PATH = "https://muignition2.webzen.co.kr/main"
  SUPPORT = (By.XPATH, "//li[@class='nav-page5']/a")
  TICKETS = (By.XPATH, "//li[@class='nav-page5']/ul/li[2]/a")