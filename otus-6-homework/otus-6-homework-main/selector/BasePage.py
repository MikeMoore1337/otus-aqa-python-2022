from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_browser(self):
        self.browser.get(self.url)

    def find_element_with_wait(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_element_with_wait_clickable(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        raise AssertionError("Не найден элемент с селектором: {}".format(locator))
