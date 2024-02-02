from selenium.webdriver.common.by import By

class SUNCLCSLocators:
  PATH_WRITE = "https://sunclassic.webzen.co.kr/support/tickets"
  PATH_LIST = "https://sunclassic.webzen.co.kr/support/tickets/list"
  PHONE = (By.XPATH, "//*[@id='txtPhone2']")  
  TITLE = (By.XPATH, "//*[@id='title']")
  CONTENT = (By.XPATH, "//*[@id='content']")  
  AGRSMS = (By.XPATH, "//*[@id='phaonArea']/td/span[2]/label/span")    
  AGRPRIVACY = (By.XPATH, "//*[@id='frmMain']/table/tbody/tr[12]/td/span/label/span")  
  WRITE = (By.XPATH, "//*[@class='write']")
  CANCEL = (By.XPATH, "//*[@class='cancel']")