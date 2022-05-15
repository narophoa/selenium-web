import unittest
from selenium import webdriver

class TestWebzenPortal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_page_load_portal(self):
        driver = self.driver
        driver.get("https://www.webzen.co.kr")
        title = self.driver.title
        assert 'Webzen - Games Portal' in title

    def test_page_load_member(self):
        driver = self.driver
        driver.get("http://member.webzen.co.kr")
        title = self.driver.title
        assert '로그인 - 웹젠' in title
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()