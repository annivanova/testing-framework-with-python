from Pages.BasePage import BasePage, InvalidPageException
from Util.locators import locators_login_page


class OuathPage(BasePage):

    def __init__(self, driver):
        super(OuathPage, self).__init__(driver)

    @property
    def get_oauth_title(self):
        title= self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[8]/a')
        return title

    @property
    def get_add_app_title(self):
        title_add = self.driver.find_element_by_xpath('//*[@id="pane2"]/div[1]/div')
        return title_add

    @property
    def get_field_name(self):
        field_name= self.driver.find_element_by_xpath('//*[@id="oauth_applications_name"]')
        return field_name

    @property
    def get_form_app(self):
        form_app= self.driver.find_element_by_xpath('//*[@id="new_oauth_application"]/div[3]')
        return form_app

    @property
    def get_btn_add_application(self):
        add_btn=self.driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/a')
        return add_btn

    @property
    def get_url_field(self):
        url_field=self.driver.find_element_by_xpath('//*[@id="oauth_applications_redirect_uri"]')
        return url_field

    @property
    def get_safe_btn(self):
        safe_btn= self.driver.find_element_by_xpath('//*[@id="new_oauth_application"]/div[3]/div[2]/input')
        return safe_btn

    @property
    def get_alert_msg(self):
        alert= self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div')
        return alert

    @property
    def get_del_button(self):
        return self.driver.find_element_by_xpath('//*[@id="drop1"]/li[2]/a')

    @property
    def get_settings_el(self):
            settings_ell=self.driver.find_element_by_xpath('//*[@id="pane3"]/div/div[1]/div[1]/a/div')
            return settings_ell

    @property
    def get_edit_btn(self):
        return self.driver.find_element_by_xpath('//*[@id="drop1"]/li[1]/a')

    @property
    def get_cancel_btn(self):
        cancel_btn=self.driver.find_element_by_xpath('//*[@id="new_oauth_application"]/div[3]/div[2]/a/span')
        return cancel_btn

    def click_cancel_btn(self):
        self.get_cancel_btn.click()

    def click_add_btn(self):
        self.get_btn_add_application.click()

    def filling_name(self, name):
        self.get_field_name.send_keys(name)

    def filling_url_field(self, url):
        self.get_url_field.send_keys(url)

    def save_form(self):
        self.get_safe_btn.click()

    def validate_msg_allert(self):
        assert self.get_alert_msg is not None

    def display_settings(self):
        self.get_settings_el.click()

    def validate_page(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[8]/a')
        except:
            raise InvalidPageException("Page is not loading")

    def validate_form(self, sel_page):
        try:
            self.driver.find_element_by_xpath(sel_page['//*[@id="new_oauth_application"]/div[3]'])
        except:
            raise InvalidPageException("form is not loaded")

    def validate_oauth_page(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[8]/a')
        except:
            raise InvalidPageException('page is not loaded')