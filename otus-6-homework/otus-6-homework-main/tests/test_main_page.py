from selector.main_page import MainPage


def test_check_name(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_name()


def test_check_cart(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_cart()


def test_check_macbook(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_macbook()


def test_check_search(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_search()


def test_check_product(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_product()
