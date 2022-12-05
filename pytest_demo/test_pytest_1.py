import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# to run => pytest test_pytest_1.py -v
# to generate report => pytest test_pytest_1.py -v -s --html=report.html


def test_verify_title():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get("http://google.com")
    assert driver.title == "Google"
    driver.quit()
