import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("global_fixture")
class TestBase:
    pass


class Test_freecrm(TestBase):

    @pytest.mark.parametrize("username, password", [("aabb1122", "aabb1122"), ("aabb2211", "aabb2211")])
    def test_login_freecrm(self, username, password):
        self.driver.get("https://classic.freecrm.com/index.html")
        self.driver.find_element(
            By.NAME, "username").send_keys(username)
        self.driver.find_element(
            By.NAME, "password").send_keys(password)
