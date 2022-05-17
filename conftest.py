import pytest
import sys
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):
  driver = webdriver.Chrome()
  driver.implicitly_wait(30)
  request.cls.driver = driver
  driver.maximize_window()

  yield
  driver.close()
