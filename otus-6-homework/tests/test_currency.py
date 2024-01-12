from selector.change_currency import Currency


def test_currency(browser, url):
    currency = Currency(browser, url)
    currency.open_browser()
    currency.change_btn()
    currency.gbr()
