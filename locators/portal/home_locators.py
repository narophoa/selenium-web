from selenium.webdriver.common.by import By

class HomepageLocators:
  PATH = "https://www.webzen.co.kr"
  GNB = (By.XPATH, "//header[@id='header']")
  BI = (By.XPATH, "//div/header/h1/a[@href]")
  CALLER = (By.XPATH, "//a[@class='caller']")
  ALL_GAME_LIST = (By.XPATH, "//a[@class='all-game-list']")
  ALL_GAME_LIST_SELECTED = (By.XPATH, "//a[@class='all-game-list selected']")
  PC_GAME_LIST = (By.XPATH, "//a[@class='pc-game-list']")
  PC_GAME_LIST_SELECTED = (By.XPATH, "//a[@class='pc-game-list selected']")
  MOBILE_GAME_LIST = (By.XPATH, "//a[@class='mobile-game-list']")
  MOBILE_GAME_LIST_SELECTED = (By.XPATH, "//a[@class='mobile-game-list selected']")
  SIGNUP = (By.XPATH, "//article[@class='member']/a[1]")
  LOGIN = (By.XPATH, "//article[@class='member']/a[2]")
  LOGOUT = (By.XPATH, "//article[@class='member']/a[2]")