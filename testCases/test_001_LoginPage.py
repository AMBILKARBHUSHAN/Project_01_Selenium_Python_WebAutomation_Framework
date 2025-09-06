"""
This file contains test cases for validating the OrangeHRM login functionality.
- Uses Pytest fixtures for browser setup (from conftest.py).
- Reads test data (URL, username, password) from config.ini using ReadConfiguration.
- Verifies successful login and page title.
"""

from pageObjects.LoginPage_objects import LoginPage     # Page Object class for login page
from utilities.readConfigurations import ReadConfiguration
from utilities.customLogger import LogGenerator

class Test_001_Login:
    """
    Test class to validate login functionality of OrangeHRM application.
    """
    baseURL = ReadConfiguration.get_url()
    log = LogGenerator.loggen()

    user = ReadConfiguration.get_username()
    password = ReadConfiguration.get_password()

    def test_homepage_title(self, setup):       # Test case to verify homepage title
        self.log.info(" ------ Test HomePage Title ------ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        assert actual_title == "OrangeHRM"
        self.driver.close()

    def test_login(self, setup):                # Test case to verify login with valid credentials
        self.log.info(" ----- Test_001_Login Page ----- ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.user)
        self.lp.enter_password(self.password)
        self.lp.click_on_login_button()

        actual_title = self.driver.title
        assert actual_title == "OrangeHRM", "Login test failed!"
        self.driver.close()


