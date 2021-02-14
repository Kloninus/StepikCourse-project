from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_URL = "/login"
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")


class ProductPageLocators:

    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    BASKET_TOTAL_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
