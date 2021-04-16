from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page_and_empty(self):
        self.should_not_be_any_goods()
        self.should_be_message_about_empty_basket()

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'Basket is not empty'

    def should_not_be_any_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), 'There are some items in basket'
