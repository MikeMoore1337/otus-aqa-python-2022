from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class CardProductSelectors:
    POSTFIX_URL = "/index.php?route=product/product&product_id=43"
    name = (By.CSS_SELECTOR, "p:nth-child(1) > b")
    price = (By.CSS_SELECTOR, "h2:nth-child(1)")
    cart = (By.ID, "button-cart")
    reviews = (By.CSS_SELECTOR, "a:nth-child(6)")
    reviews_write = (By.CSS_SELECTOR, "p > a:nth-of-type(2)")
    link = (By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")


class CardProduct(BasePage):
    def open_page(self, url):
        self.browser.get(url + CardProductSelectors.POSTFIX_URL)

    def check_name(self):
        name = self.find_element_with_wait(CardProductSelectors.name)
        return name

    def check_price(self):
        price = self.find_element_with_wait(CardProductSelectors.price)
        return price

    def check_cart(self):
        cart = self.find_element_with_wait(CardProductSelectors.cart)
        return cart

    def check_reviews(self):
        reviews = self.find_element_with_wait(CardProductSelectors.reviews)
        return reviews

    def check_write_reviews(self):
        reviews_write = self.find_element_with_wait(CardProductSelectors.reviews_write)
        return reviews_write

    def should_be_price(self):
        assert self.find_element_with_wait(CardProductSelectors.price), '$602.00'

    def should_be_name(self):
        assert self.find_element_with_wait(CardProductSelectors.name), 'Intel Core 2 Duo processor'

    def should_be_cart(self):
        assert self.find_element_with_wait(CardProductSelectors.cart), 'Add to Cart'

    def should_be_reviews(self):
        assert self.find_element_with_wait(CardProductSelectors.reviews), '0 reviews'

    def should_be_reviews_write(self):
        assert self.find_element_with_wait(CardProductSelectors.reviews_write), 'Write a review'

    def open_link(self):
        self.find_element_with_wait(CardProductSelectors.link).click()
