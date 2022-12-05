import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope='class', params=["chrome", "firefox"])
def global_fixture(request):
    print("--------------------------------Test execution started--------------------------------")
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        service = FirefoxService(log_path='nul')
        driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(2)

    yield
    print("--------------------------------Test execution finished--------------------------------")
    driver.quit()
