from selenium.webdriver.common.by import By

class Mui2pageLocators:
  PATH = "https://muignition2.webzen.co.kr/main"
  PATH_NOTICE = "https://muignition2.webzen.co.kr/news/notices"
  PATH_GMNOTE = "https://muignition2.webzen.co.kr/news/gm-note"
  PATH_EVENTS = "https://muignition2.webzen.co.kr/news/events"
  PATH_INTRODUCE = "https://muignition2.webzen.co.kr/guides/introduce/"
  PATH_CHARACTER = "https://muignition2.webzen.co.kr/guides/characters"
  PATH_BEGINNER = "https://muignition2.webzen.co.kr/guides/beginner/requirement"
  PATH_GAMEGUIDE = "https://muignition2.webzen.co.kr/guides/gameguides"
  PATH_PROBABILITY = "https://muignition2.webzen.co.kr/guides/probability"
  PATH_RANKING = "https://muignition2.webzen.co.kr/ranking"
  PATH_LEVEL = "https://muignition2.webzen.co.kr/ranking/level"
  PATH_FREEBOARD = "https://muignition2.webzen.co.kr/community/free-board"
  PATH_JOINEVENT = "https://muignition2.webzen.co.kr/community/joinevent"
  PATH_FAQ = "https://muignition2.webzen.co.kr/support/faq"
  PATH_TICKETS = "https://muignition2.webzen.co.kr/support/tickets"
  PATH_POLICY = "https://muignition2.webzen.co.kr/support/policy"
  PATH_OPERATION = "https://muignition2.webzen.co.kr/news/operation"
  PATH_DOWNLOAD = "https://muignition2.webzen.co.kr/support/download"
  PATH_SHOP = "https://muignition2.webzen.co.kr/shop"
  PATH_STORAGE = "https://muignition2.webzen.co.kr/shop/storage/storagelist"  
  PCBANG_BENEFIT_ON = (By.XPATH, "//*[@class='aside__pcbang__on']")
  PCBANG_BENEFIT_OFF = (By.XPATH, "//*[@class='aside__pcbang__off']")
  TOPBAR_LOGIN_BUTTON = (By.XPATH, "//*[@class='before-login']/a[2]")
  TOPBAR_LOGOUT_BUTTON = (By.XPATH, "//*[@class='after-login']/a[3]")