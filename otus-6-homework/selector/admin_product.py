from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class LoginAdminSelector:
    POSTFIX_URL = "/admin"
    login = (By.CSS_SELECTOR, "#input-username")
    password = (By.CSS_SELECTOR, "#input-password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    catalog = (By.CSS_SELECTOR, "li#menu-catalog > .collapsed.parent")
    products = (By.LINK_TEXT, "Products")


class AddProductSelector:
    add_new = (By.CSS_SELECTOR, ".pull-right > a")
    name_product = (By.CSS_SELECTOR, "#input-name1")
    meta_teg = (By.CSS_SELECTOR, "#input-meta-title1")
    link_data = (By.LINK_TEXT, "Data")
    model = (By.CSS_SELECTOR, "#input-model")
    save = (By.CSS_SELECTOR, "button[type='submit']")


class DeleteProductSelector:
    delete = (By.CSS_SELECTOR, ".btn-danger")
    accept_product = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) [type]")


class Login(BasePage):

    def open(self, url):
        self.browser.get(url + LoginAdminSelector.POSTFIX_URL)

    def input_login(self):
        login = self.find_element_with_wait(LoginAdminSelector.login).send_keys("user")
        return login

    def input_password(self):
        password = self.find_element_with_wait(LoginAdminSelector.password).send_keys("bitnami")
        return password

    def login_button(self):
        login_button = self.find_element_with_wait(LoginAdminSelector.login_button).click()
        return login_button

    def catalog(self):
        catalog = self.find_element_with_wait(LoginAdminSelector.catalog).click()
        return catalog

    def products(self):
        products = self.find_element_with_wait(LoginAdminSelector.products).click()
        return products


class AddProduct(BasePage):

    def input_name_product(self):
        name_product = self.find_element_with_wait(AddProductSelector.name_product).send_keys("123456789")
        return name_product

    def input_meta_teg(self):
        meta_teg = self.find_element_with_wait(AddProductSelector.meta_teg).send_keys("123456789")
        return meta_teg

    def link_data(self):
        link_data = self.find_element_with_wait(AddProductSelector.link_data).click()
        return link_data

    def input_model(self):
        model = self.find_element_with_wait(AddProductSelector.model).send_keys("123456")
        return model

    def save(self):
        save = self.find_element_with_wait(AddProductSelector.save).click()
        return save

    def add_new(self):
        add = self.find_element_with_wait(AddProductSelector.add_new).click()
        return add


class DeleteProduct(BasePage):

    def delete(self):
        delete = self.find_element_with_wait(DeleteProductSelector.delete).click()
        return delete

    @property
    def assert_confirmation(self):
        alert = self.browser.switch_to.alert.accept()
        return alert

    def accept_product(self):
        accept_product = self.find_element_with_wait(DeleteProductSelector.accept_product).click()
        return accept_product
