from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        login_link.click()

    def should_be_title_add_message(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_ADD_MESSAGE).text
        book_title_expected = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert book_title == book_title_expected, f"Invalid book title, add '{book_title_expected}' bit in add message '{book_title}' "

    def should_be_right_price_in_basket(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_ADD_MESSAGE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert basket_price == book_price, f"Invalid basket total price, expected '{book_price}' exist '{basket_price}'"
