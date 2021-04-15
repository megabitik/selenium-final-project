from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_BUY_ITEM = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    ALL_MESSAGES = (By.CSS_SELECTOR, '#messages>div.alert-success strong')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    BASKET_MINI = (By.CSS_SELECTOR, 'div.basket-mini')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    MESSAGE_ANY = (By.CSS_SELECTOR, '#messages>div.alert-success')
