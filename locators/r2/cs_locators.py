from selenium.webdriver.common.by import By

class R2CSLocators:
  PATH_WRITE = "https://r2.webzen.co.kr/support/tickets"
  PATH_LIST = "https://r2.webzen.co.kr/support/tickets/list"
  PHONE = (By.XPATH, "//*[@id='txtPhone']")
  TITLE = (By.XPATH, "//*[@id='title']")
  CONTENT = (By.XPATH, "//*[@id='content']")
  AGRPRIVACY = (By.XPATH, "//*[@id='frmMain']/div/table/tbody/tr[12]/td/span")
  WRITE = (By.XPATH, "//*[@id='frmMain']/div/div[2]/a")
  CANCEL = (By.XPATH, "//*[@id='contents']/div/div/div/div[2]/table/tbody/tr[1]/td[6]/a")