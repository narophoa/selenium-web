from selenium.webdriver.common.by import By

class SUNCLpageLocators:
  PATH = "https://sunclassic.webzen.co.kr/main"
  PATH_NOTICE = "https://sunclassic.webzen.co.kr/news/notices"
  PATH_UPDATE = "https://sunclassic.webzen.co.kr/news/update"
  PATH_GMNOTE = "https://sunclassic.webzen.co.kr/news/gm-note"
  PATH_EVENTS = "https://sunclassic.webzen.co.kr/news/events"
  PATH_INTRODUCE = "https://sunclassic.webzen.co.kr/gameinfo/guide/detail/2018"
  PATH_CHARACTER = "https://sunclassic.webzen.co.kr/gameinfo/guide/detail/2019"  
  PATH_GAMEGUIDE = "https://sunclassic.webzen.co.kr/gameinfo"
  PATH_PROBABILITY = "https://sunclassic.webzen.co.kr/guides/probability"
  PATH_FREEBOARD = "https://sunclassic.webzen.co.kr/community/free-board"
  PATH_IMAGEBOARD = "https://sunclassic.webzen.co.kr/community/image-board"
  PATH_ATTACKBOARD = "https://sunclassic.webzen.co.kr/community/attack-board"
  PATH_FAQ = "https://sunclassic.webzen.co.kr/support/faq"
  PATH_TICKETS = "https://sunclassic.webzen.co.kr/support/tickets"
  PATH_POLICY = "https://sunclassic.webzen.co.kr/support/policy"
  PATH_COUPON = "https://sunclassic.webzen.co.kr/support/coupon"
  PATH_DOWNLOAD = "https://sunclassic.webzen.co.kr/support/download"    
  PCBANG_BENEFIT_ON = (By.XPATH, "//*[@id='pabangLayerON']") 
  PCBANG_BENEFIT_OFF = (By.XPATH, "//*[@id='pabangLayerOff']")
  TOPBAR_LOGIN_BUTTON = (By.XPATH, "//*[@class='before-login']/a[2]")
  TOPBAR_LOGOUT_BUTTON = (By.XPATH, "//*[@class='after-login']/a[3]")
  SITE_LOGIN_BUTTON = (By.XPATH, "//*[@class='btn-login']")
  SITE_LOGOUT_BUTTON = (By.XPATH, "//*[@class='login-menu']/a[2]")