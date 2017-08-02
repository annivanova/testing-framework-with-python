from unittest import TestCase
from selenium import webdriver


class BaseTest(TestCase):
    time_out = 5

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(self.time_out)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://demo.fluxday.io')

    def tearDown(self):
        # close the browser window
        self.driver.quit()
