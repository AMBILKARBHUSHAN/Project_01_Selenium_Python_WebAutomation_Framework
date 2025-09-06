"""
This file manages browser setup using Pytest fixtures.
- Adds a custom CLI option (--browser) to choose the browser at runtime.
- Initializes the WebDriver instance based on the given browser.
- Applies implicit wait and maximizes the window.
- Returns the driver instance for use in tests.
"""

from selenium import webdriver
import pytest


def pytest_addoption(parser):                 # Hook to add a custom CLI option (--browser) for test execution
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                         # Fixture to fetch the browser value passed from CLI
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):                           # Fixture to initialize WebDriver instance based on browser input
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching the Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching the Firefox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching the Edge browser")
    else:
        print("Headless mode")
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(options=option)

    driver.implicitly_wait(10)                # Instructs WebDriver to poll the DOM for up to 10 seconds when trying to find an element before throwing an exception.
    driver.maximize_window()                  # Maximizes the browser window for better visibility
    return driver                             # Returns the driver instance for test execution
