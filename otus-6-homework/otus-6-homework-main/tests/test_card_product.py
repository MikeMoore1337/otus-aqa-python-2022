from selector.card_product import CardProduct


def test_check_name(browser, url):
    name = CardProduct(browser, url)
    name.open_browser()
    name.open_link()
    name.check_name()
    name.should_be_name()


def test_check_price(browser, url):
    price = CardProduct(browser, url)
    price.open_browser()
    price.open_link()
    price.check_price()
    price.should_be_price()


def test_check_cart(browser, url):
    cart = CardProduct(browser, url)
    cart.open_browser()
    cart.open_link()
    cart.check_cart()
    cart.should_be_cart()


def test_check_reviews(browser, url):
    reviews = CardProduct(browser, url)
    reviews.open_browser()
    reviews.open_link()
    reviews.check_reviews()
    reviews.should_be_reviews()


def test_check_reviews_write(browser, url):
    reviews_write = CardProduct(browser, url)
    reviews_write.open_browser()
    reviews_write.open_link()
    reviews_write.check_write_reviews()
    reviews_write.should_be_reviews_write()
