import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# to run => pytest test_pytest_1.py -v
# to generate report => pytest test_pytest_1.py -v -s --html=report.html

driver = None

# dont change below function name
# setup_module(module) -> this will be treat as @BeforeMethod
# teardown_module(module) -> this will be treat as @AfterMethod


def setup_module(module):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get("http://google.com")


def test_verify_title():
    assert driver.title == "Google"


def test_verify_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"


def teardown_module(module):
    driver.quit()
