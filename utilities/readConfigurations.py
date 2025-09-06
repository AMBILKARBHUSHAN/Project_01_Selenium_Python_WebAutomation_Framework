"""
This file provides utility methods to read application configuration
details from the config.ini file.
- Centralizes test configuration like URL, username, and password.
- Makes the framework flexible by avoiding hardcoding of values.
"""

import configparser

# Create a RawConfigParser object to read configuration files
config = configparser.RawConfigParser()

# Load the config.ini file containing project configuration details
config.read("E:\\OrangeHRM\\configuration\\config.ini")


class ReadConfiguration:
    """
    Utility class to fetch application configuration details
    such as URL, username, and password from config.ini file.
    """

    @staticmethod
    def get_url():                # Returns the application URL from config.ini
        url = config.get("common info", "Url")
        return url

    @staticmethod
    def get_username():           # Returns the username from config.ini
        username = config.get("common info", "Username")
        return username

    @staticmethod
    def get_password():           # Returns the password from config.ini
        password = config.get("common info", "Password")
        return password
