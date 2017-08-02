import unittest
from Tests.BaseTest import BaseTest
from Util.AjaxHelper import AjaxHelper
from Pages.OAuthPage import OuathPage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


class OauthTest(BaseTest):

    def test_oauth_btn(self):
        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')

        #testing the functionality of the oauth application button on the homepage
        oauth = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        oauth.click_oauthapp_btn()
        self.driver.implicitly_wait(7)

        add_title = OuathPage(self.driver)
        add_title.validate_oauth_page()

        # testing the functionality of the add_application button
    def test_add_btn(self):

        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')

        oauth = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        oauth.click_oauthapp_btn()

        add_btn=OuathPage(self.driver)
        add_btn.click_add_btn()
        self.driver.implicitly_wait(7)
        add_btn.validate_page()

        # testing the functionality of the oauth form and the save button on the oauth form
    def test_form(self):

        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')

        oauth = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        oauth.click_oauthapp_btn()

        add_btn = OuathPage(self.driver)
        add_btn.click_add_btn()
        self.driver.implicitly_wait(7)

        field_name = OuathPage(self.driver)
        self.driver.implicitly_wait(10)
        field_name.filling_name('peter')
        url_name=OuathPage(self.driver)
        url_name.filling_url_field('https://en.wikipedia.org/wiki/OAuth')
        save_form=OuathPage(self.driver)
        save_form.save_form()
        msg_alert=OuathPage(self.driver)
        msg_alert.validate_msg_allert()
        msg_alert.validate_msg_allert()

        # testing the functionality of the settings button
    def test_settings_btn(self):

        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')

        oauth = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        oauth.click_oauthapp_btn()
        self.driver.implicitly_wait(7)

        add_btn = OuathPage(self.driver)
        add_btn.click_add_btn()
        self.driver.implicitly_wait(7)

        field_name = OuathPage(self.driver)
        self.driver.implicitly_wait(10)
        field_name.filling_name('peter')
        url_name = OuathPage(self.driver)
        url_name.filling_url_field('https://en.wikipedia.org/wiki/OAuth')
        save_form = OuathPage(self.driver)
        save_form.save_form()
        msg_alert = OuathPage(self.driver)
        msg_alert.validate_msg_allert()

        settings_el=OuathPage(self.driver)
        settings_el.display_settings()
        edit_btn=OuathPage(self.driver)
        delete_btn=OuathPage(self.driver)
        self.assertTrue( edit_btn.get_edit_btn and delete_btn.get_del_button)

        # testing the functionality of the cancel button on the oauth form
    def test_cancel_btn(self):

        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')

        oauth = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        oauth.click_oauthapp_btn()

        add_btn = OuathPage(self.driver)
        add_btn.click_add_btn()
        self.driver.implicitly_wait(7)

        cancel_btn=OuathPage(self.driver)
        cancel_btn.click_cancel_btn()
        add_btn.validate_oauth_page()


if __name__ == "__main__":
    unittest.main(verbosity=2)