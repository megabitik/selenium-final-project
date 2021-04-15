from .base_page import BasePage
from .locators import ProductPageLocators
import re

class ProductPage(BasePage):
    def _make_float(self, s: str):
        try:
            return float(s)
        except ValueError:
            return False

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_BUY_ITEM).click()

    def should_be_matching_book_names(self):
        messages_strong = [m.text for m in self.browser.find_elements(*ProductPageLocators.ALL_MESSAGES)]
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name in messages_strong, f'Book name {book_name} ' \
                                             f'was not found in <strong> messages: {messages_strong}'

    def should_be_equal_book_price_and_basket(self):
        pattern_price = r'(\d+(\.\d+)?)'  # RegExt takes float/int part from text, better check with .isnumeric()
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        basket_cost = self._make_float(re.findall(pattern_price, basket_cost).pop()[0])
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price = self._make_float(re.findall(pattern_price, book_price).pop()[0])
        assert basket_cost, f'Mini basket cost is {basket_cost}, but must be int or float'
        assert book_price, f'Book price is {book_price}, but must be int or float'
        assert basket_cost == book_price, f"Basket price ({basket_cost}) and book price ({book_price}) aren't equal"