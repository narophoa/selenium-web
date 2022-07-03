import pytest
import sys
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):
  driver = webdriver.Chrome()
  # 암시적/묵시적 대기, 최대 시간
  driver.implicitly_wait(30)
  request.cls.driver = driver
  driver.maximize_window()

  yield
  driver.close()
