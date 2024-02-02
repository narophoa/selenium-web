from selenium.webdriver.common.by import By

class LoginpageLocators:
  PATH = "https://www.shotonline.co.kr/login"
  ID = (By.XPATH, "//*[@id='uid']")
  PASSWORD = (By.XPATH, "//*[@id='upass']")
  LOGIN_BUTTON = (By.XPATH, "//*[@id='loginform']/fieldset/a")
  LOGOUT_BUTTON = (By.XPATH, "//*[@id='shotWrap']/div[3]/div[1]/div[2]/div[1]/div/div/a[3]")   #홈화면에 있는 로그아웃 버튼
