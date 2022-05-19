from selenium.webdriver.common.by import By

class LoginpageLocators:
  PATH = "https://member.webzen.co.kr"
  ID = (By.XPATH, "//*[@id='AccountID']")
  PASSWORD = (By.XPATH, "//*[@id='Password']")
  LOGIN_BUTTON = (By.XPATH, "//*[@id='contents']/div[1]/fieldset/div/button")
  CHANGE_PASSWORD = (By.XPATH, "//*[@id='contents']/div/div/a[2]")