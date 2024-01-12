from selector.catalog import Catalog


def test_check_desktops(browser, url):
    desktops = Catalog(browser, url)
    desktops.open(url)
    desktops.check_desktop()
    desktops.check_mac()
    desktops.mac_check()


def test_check_components(browser, url):
    components = Catalog(browser, url)
    components.open(url)
    components.check_components()
    components.check_monitors()
    components.monitors_check()


def test_check_tablets(browser, url):
    tablets = Catalog(browser, url)
    tablets.open(url)
    tablets.tablets_check()
    tablets.check_tablets()


def test_check_software(browser, url):
    software = Catalog(browser, url)
    software.open(url)
    software.software_check()
    software.software_check()


def test_check_phone(browser, url):
    phone = Catalog(browser, url)
    phone.open(url)
    phone.check_phone()
    phone.phones_check()
