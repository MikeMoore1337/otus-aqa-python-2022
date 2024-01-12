from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class CatalogSelector:
    POSTFIX_URL = "/desktops"
    desktops = (By.CSS_SELECTOR, "div#content > h2")
    mac = (By.XPATH, "//a[contains(text(),'Mac (1)')]")
    check_mac = (By.CSS_SELECTOR, "h2")
    components = (By.XPATH, "//a[contains(text(),'Components')]")
    monitors = (By.XPATH, "//a[contains(text(),'Monitors (2)')]")
    check_monitors = (By.CSS_SELECTOR, "h2")
    tablets = (By.XPATH, "//a[contains(text(),'Tablets')]")
    check_tablets = (By.CSS_SELECTOR, "h2")
    software = (By.XPATH, "//a[contains(text(),'Software')]")
    check_software = (By.CSS_SELECTOR, "h2")
    phones = (By.XPATH, "//a[contains(text(),'Phones & PDAs')]")
    check_phones = (By.CSS_SELECTOR, "h2")


class Catalog(BasePage):

    def open(self, url):
        self.browser.get(url + CatalogSelector.POSTFIX_URL)

    def check_desktop(self):
        desktop = self.find_element_with_wait(CatalogSelector.desktops)
        return desktop

    def check_mac(self):
        mac = self.find_element_with_wait(CatalogSelector.mac)
        return mac

    def check_components(self):
        components = self.find_element_with_wait(CatalogSelector.components)
        return components

    def check_monitors(self):
        monitors = self.find_element_with_wait(CatalogSelector.monitors)
        return monitors

    def check_tablets(self):
        tablets = self.find_element_with_wait(CatalogSelector.tablets)
        return tablets

    def check_software(self):
        software = self.find_element_with_wait(CatalogSelector.software)
        return software

    def check_phone(self):
        phone = self.find_element_with_wait(CatalogSelector.phones)
        return phone

    def mac_check(self):
        mac_check = self.find_element_with_wait(CatalogSelector.check_mac)
        return mac_check

    def monitors_check(self):
        monitors_check = self.find_element_with_wait(CatalogSelector.check_monitors)
        return monitors_check

    def tablets_check(self):
        tablets_check = self.find_element_with_wait(CatalogSelector.check_tablets)
        return tablets_check

    def software_check(self):
        software_check = self.find_element_with_wait(CatalogSelector.check_software)
        return software_check

    def phones_check(self):
        phones_check = self.find_element_with_wait(CatalogSelector.check_phones)
        return phones_check
