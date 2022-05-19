import inspect
from config.config import TIMEOUT
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage():

  def __init__(self, driver):
    self.driver = driver

  # get current page title
  def get_title(self):
    return self.driver.title

  # get current page url
  def get_url(self):
    return self.driver.current_url

  # get browser cookies
  def get_cookie(self, name):
    return self.driver.get_cookie(name)

  # page open url
  def open_url(self, path):
    self.driver.get(path)

  # element click
  def click(self, locator):
    el = WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(locator))
    el.click()

  # move to element
  def mouseover(self, locator):
    # el = WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_selected(locator))
    self.move_to_element(locator)

  # find element instance
  def find_element(self, locator):
    return self.driver.find_element(locator[0], locator[1])

  # element send keys
  def send_keys(self, locator, input):
    self.find_element(locator).clear()
    self.find_element(locator).send_keys(input)