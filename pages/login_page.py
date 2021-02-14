from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        current_url = str(self.browser.current_url)
        expected_url = LoginPageLocators.LOGIN_URL
        assert expected_url in current_url, f"Invalid login URL, '{current_url}' don't include {expected_url} "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Missed login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Missed register form"
