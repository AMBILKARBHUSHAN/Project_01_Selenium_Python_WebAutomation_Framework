"""
This file contains the Page Object Model (POM) implementation for the OrangeHRM Login Page.
- Encapsulates the locators and actions (enter username, enter password, click login).
- Provides reusable methods for login-related interactions.
"""

from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object class for OrangeHRM Login Page.
    Contains element locators and methods to perform login actions.
    """

    # Locators for login page elements
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@type='password']"
    login_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):                       # Constructor to initialize WebDriver instance
        self.driver = driver

    def enter_username(self, username):               # Method to enter username into the username field
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_password(self, password):               # Method to enter password into the password field
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_on_login_button(self):                  # Method to click on the login button
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
