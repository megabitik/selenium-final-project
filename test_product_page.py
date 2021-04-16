from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.xfail(reason='Going to be deleted. Stepik said to comment out.')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ANY), 'Guest can see success message FAILED'

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_page_and_empty()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ANY), "Guest can't see success message FAILED"

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.xfail(reason='Going to be deleted. Stepik said to comment out.')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    assert page.is_disappeared(*ProductPageLocators.MESSAGE_ANY), "Message didn't disappear after adding to basket"

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_matching_book_names()
    page.should_be_equal_book_price_and_basket()


