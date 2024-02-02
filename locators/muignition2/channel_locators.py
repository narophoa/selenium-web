from selenium.webdriver.common.by import By

class Mui2ChannelLocators:
  PATH_NAVER = "https://muignition2.game.naver.com/main"
  NAVER_LOGIN_BUTTON = (By.XPATH, "//*[@id='header']/section/div[1]/article/a/img")
  NAVER_LOGIN_ID = (By.XPATH, "//*[@id='id']")
  NAVER_LOGIN_PW = (By.XPATH, "//*[@id='pw']")
  NAVER_LOGIN_SUBMIT = (By.XPATH, "//*[@id='log.login']")
