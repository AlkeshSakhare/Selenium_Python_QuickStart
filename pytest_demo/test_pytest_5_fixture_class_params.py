import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

# statement before yield will treated as @BeforeMethod and after yield will be treated as @AfterMethod
# fixture can be defined as class/module -> @pytest.fixture(scope='class') and can be applied in 2 ways as below
# Way 1: fixture can be applied to test_function() as-> fixture function name need to pass in test_function()
# Way 2: fixture can be applied to test_function() as annotation like -> @pytest.mark.usefixtures("init_driver")

# Way 1 recommended for module level fixture
# Way 2 recommended for class level fixture

# params can be applied to pass parameter in test e.g. browser name and which can be use in test


@pytest.fixture(scope='class', params=["chrome", "firefox"])
def init_driver(request):
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


@pytest.mark.usefixtures("init_driver")
class TestBase:
    pass


class Test_Google(TestBase):

    def test_verify_title(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"

    def test_verify_url(self):
        self.driver.get("http://google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
