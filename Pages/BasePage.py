
from abc import abstractmethod

from Util.AjaxHelper import AjaxHelper
from Util.locators import locators_home_page


class BasePage:
    """This is the super class of all pages, all pages inherit from it"""

    def __init__(self, driver):
        self.driver = driver
        self._validate_page()

    @property
    def get_oauth_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_oauth'])

    def go_to_oauth(self):
        self.get_oauth_link.click()
        AjaxHelper.suspend(2)
        from Pages.OAuthPage import OAuthPage
        return OAuthPage(self.driver)

    @abstractmethod
    def _validate_page(self):
        pass


class InvalidPageException(Exception):
    """Throw this exception when you don't find the correct page"""