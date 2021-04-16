from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import DeleteProfile
from .locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL doesn't contain 'login' word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Login form is not found'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_NEW_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_NEW_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_REGISTRATION_SUCCESS),\
            'Registration failed. Terminating the rest of the test'

    def delete_profile(self, password):
        assert self.is_appeared(*BasePageLocators.USER_ICON), 'Delete Profile: User Icon not found'
        self.browser.find_element(*BasePageLocators.USER_ICON).click()
        assert self.is_appeared(*DeleteProfile.DP_BUTTON), 'Delete Profile: Button "Delete profile" not found'
        self.browser.find_element(*DeleteProfile.DP_BUTTON).click()
        assert self.is_appeared(*DeleteProfile.DP_CONFIRM_INPUT_PASS), \
                                                            'Delete Profile: password confirmation field not found'
        self.browser.find_element(*DeleteProfile.DP_CONFIRM_INPUT_PASS).send_keys(password)
        self.browser.find_element(*DeleteProfile.DP_BUTTON_CONFIRM_DELETION).click()