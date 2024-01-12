from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class CurrencySelector:
    change_btn = (By.CSS_SELECTOR, ".btn-group>.btn-link")
    gbr = (By.CSS_SELECTOR, "li:nth-child(2)>.currency-select")


class Currency(BasePage):
    def change_btn(self):
        change_btn = self.find_element_with_wait(CurrencySelector.change_btn).click()
        return change_btn

    def gbr(self):
        gbr = self.find_element_with_wait(CurrencySelector.gbr).click()
        return gbr
