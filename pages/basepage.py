from ast import Pass
import inspect
from config.config import TIMEOUT
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

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
  
  # Alerts accpet
  def alert_accept(self):
    try:
      result = Alert(self.driver) 
      result.accept()
    except:
      Pass
  
  # Alerts dismiss
  def alert_dismiss(self):
    try:
      result = Alert(self.driver) 
      result.dismiss()
    except:
      Pass

  # Confirm
  def alert_confirm(self):    
    try:
      result = self.driver.switch_to.alert
      result.accept()
    except:
      print("no alert")    

  # enter
  def enter(self):
    self.send_keys(Keys.ENTER)

  # switch
  def switch_to_window_2(self):
    self.driver.switch_to.window(self.driver.window_handles[2])

  def switch_to_window_1(self):
    self.driver.switch_to.window(self.driver.window_handles[1])

  def switch_to_window_0(self):
    self.driver.switch_to.window(self.driver.window_handles[0])

  # iframe 인덱스 사용하여 전환
  def switch_to_iframe_index(self):
    self.driver.switch_to.frame(0)
  
  # iframe 빠져나와서 기본 콘텐츠로 돌아가기
  def switch_to_iframe_return(self):
    self.driver.switch_to_default_content()
