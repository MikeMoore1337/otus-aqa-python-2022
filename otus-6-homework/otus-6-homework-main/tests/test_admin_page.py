from selector.admin_page import AdminPage


def test_check_img(browser, url):
    img = AdminPage(browser, url)
    img.open(url)
    img.check_img()


def test_check_username(browser, url):
    username = AdminPage(browser, url)
    username.open(url)
    username.check_username()


def test_check_password(browser, url):
    password = AdminPage(browser, url)
    password.open(url)
    password.check_password()


def test_check_login_button(browser, url):
    login_button = AdminPage(browser, url)
    login_button.open(url)
    login_button.check_login()


def test_check_panel(browser, url):
    panel = AdminPage(browser, url)
    panel.open(url)
    panel.check_panel()
