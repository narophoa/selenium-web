import inspect
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage():

  def setUp(self):
    self.driver = webdriver.Chrome()

  # get current page title
  def get_title(self):
    return self.driver.title

  # get current page url
  def get_url(self):
    return self.driver.current_url

  # page open url
  def open_url(self, path):
    self.driver.get(path)