from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_matching_book_names()
    page.should_be_equal_book_price_and_basket()


