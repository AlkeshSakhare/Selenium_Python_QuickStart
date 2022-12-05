import pytest


@pytest.mark.usefixtures("global_fixture")
class TestBase:
    pass


class Test_Google(TestBase):

    def test_verify_title(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"

    def test_verify_url(self):
        self.driver.get("http://google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
