import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser for run tests")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/drivers/"), help="Path to drivers")
    parser.addoption("--url", action="store", default="http://192.168.1.59:8081/", help="default url")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser_name == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    elif browser_name == 'yandex':
        driver = webdriver.Chrome(executable_path=drivers + '/yandexdriver')
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=drivers + "/msedgedriver")
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")

    def fin():
        driver.close()
    request.addfinalizer(fin)

    driver.maximize_window()
    driver.url = url
    return driver
