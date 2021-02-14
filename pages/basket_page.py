from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_empty_check = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_CHEK).text
        basket_empty = BasketPageLocators.EMPTY_BASKET
        assert basket_empty_check == basket_empty, f"No empty basket message, expected '{basket_empty}'" \
                                                   " exist '{basket_empty_check}' "

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product is presented, but should not be"

