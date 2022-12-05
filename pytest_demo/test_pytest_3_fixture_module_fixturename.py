import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# statement before yield will treated as @BeforeMethod and after yield will be treated as @AfterMethod
# fixture can be defined as -> @pytest.fixture(scope='module')
# fixture can be applied to test_function() as-> fixture function name need to pass in test_function()

driver = None


@pytest.fixture(scope='module')
def init_driver():
    print("--------------------------------Test execution started--------------------------------")
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get("http://google.com")

    yield
    print("--------------------------------Test execution finished--------------------------------")
    driver.quit()


def test_verify_title(init_driver):
    assert driver.title == "Google"


def test_verify_url(init_driver):
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
