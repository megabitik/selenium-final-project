from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_NEW_EMAIL = (By.ID, 'id_registration-email')
    INPUT_NEW_PASSWORD = (By.ID, 'id_registration-password1')
    INPUT_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    BUTTON_REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
    MESSAGE_REGISTRATION_SUCCESS = (By.CSS_SELECTOR, "#messages>div.alert-success")


class ProductPageLocators:
    BUTTON_BUY_ITEM = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    ALL_MESSAGES = (By.CSS_SELECTOR, '#messages>div.alert-success strong')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    BASKET_MINI = (By.CSS_SELECTOR, 'div.basket-mini')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    MESSAGE_ANY = (By.CSS_SELECTOR, '#messages>div.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini>.btn-group>a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_GOODS = (By.ID, 'basket_formset')


class DeleteProfile:
    DP_BUTTON = (By.ID, 'delete_profile')
    DP_CONFIRM_INPUT_PASS = (By.ID, 'id_password')
    DP_BUTTON_CONFIRM_DELETION = (By.CSS_SELECTOR, 'button.btn-danger')