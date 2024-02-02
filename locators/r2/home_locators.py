from selenium.webdriver.common.by import By

class R2pageLocators:
  PATH = "https://r2.webzen.co.kr/main"
  PATH_NOTICES = "https://r2.webzen.co.kr/news/notices"
  PATH_UPDATES = "https://r2.webzen.co.kr/news/updates"
  PATH_EVENTS = "https://r2.webzen.co.kr/news/events"
  PATH_HISTORY = "https://r2.webzen.co.kr/news/history"
  PATH_PCBANG_GO = "https://r2.webzen.co.kr/events/pcbangs3/busan"
  PATH_GAME_FEATURES = "https://r2.webzen.co.kr/guides/game-features"
  PATH_SERVER_GUIDE = "https://r2.webzen.co.kr/guides/server-guides"
  PATH_BOOT_CAMP = "https://r2.webzen.co.kr/guides/boot-camp"
  PATH_GAME_GUIDE = "https://r2.webzen.co.kr/guides/game-guides"
  PATH_SUPPLY = "https://r2.webzen.co.kr/events/supply/gate"
  PATH_GUILD_WAR = "https://r2.webzen.co.kr/history/guild-war"
  PATH_SEIGE = "https://r2.webzen.co.kr/history/siege"
  PATH_RANKING = "https://r2.webzen.co.kr/history/ranking"
  PATH_TOURNAMENT7 = "https://r2.webzen.co.kr/events/tournament7"
  PATH_FREE_BOARD = "https://r2.webzen.co.kr/community/free-board"
  PATH_IMAGE_BOARD = "https://r2.webzen.co.kr/community/image-board"
  PATH_TIP_BOARD = "https://r2.webzen.co.kr/community/tip-board"
  PATH_GM_NOTE = "https://r2.webzen.co.kr/community/gm-note"
  PATH_GAME_DOWNLOAD = "https://r2.webzen.co.kr/data/game-download"
  PATH_MEDIA = "https://r2.webzen.co.kr/data/media"
  PATH_R2SHOP = "https://r2shop.webzen.co.kr/Main"
  PATH_R2MYSHOP = "https://r2shop.webzen.co.kr/Storage/StorageList"
  PATH_MYCASH = "https://payment.webzen.co.kr/history/chargecash"
  PATH_FAQ = "https://r2.webzen.co.kr/support/faq"
  PATH_TICKETS = "https://r2.webzen.co.kr/support/tickets"
  PATH_SECURITY_CARD = "https://r2.webzen.co.kr/support/security-card"
  PATH_POLICY = "https://r2.webzen.co.kr/support/policy"  
  PCBANG_BENEFIT_ON = (By.XPATH, "//*[@id='header']/section/div[2]/div/div[1]/strong/em)")  
  PCBANG_BENEFIT_OFF = (By.XPATH, "//*[@id='header']/section/div[2]/div/div[1]/strong/em)")
  TOPBAR_LOGIN_BUTTON = (By.XPATH, "//*[@id='game_code_09']/div[1]/div/div[2]/a[2]")
  SHOP_TOPBAR_LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/a[2]")
  TOPBAR_LOGOUT_BUTTON = (By.XPATH, "//*[@id='game_code_09']/div[1]/div/div[2]/a[3]")
  SITE_LOGIN_BUTTON = (By.XPATH, "//*[@id='btnWebzen']")
  SITE_LOGOUT_BUTTON = (By.XPATH, "//*[@id='header']/section/div[2]/div/div[2]/span[3]/a[3]")
  PCBANG_BENEFIT_ON = (By.XPATH, "//*[@id='header']/section/div[2]/div/div[1]/strong/em")
