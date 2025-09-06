"""
This file provides an advanced logging utility for the framework.
- Creates a dynamic logger using the calling function's name.
- Logs are stored in 'Logs/Automation.log'.
- Log format includes timestamp, log level, logger name, function name, line number, and message.
"""

import inspect
import logging


class LogGenerator:
    """
    Utility class to configure and generate detailed logs.
    Provides granular control over logging for large frameworks.
    """

    @staticmethod
    def loggen():
        # Get the name of the calling function/module dynamically
        name = inspect.stack()[1][3]

        # Create a logger with the dynamic name
        logger = logging.getLogger(name)

        # Define log file location
        logfile = logging.FileHandler("E:\\OrangeHRM\\logs\\Automation.log")

        # Define log format with detailed information
        format = logging.Formatter(
            " %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s"
        )
        logfile.setFormatter(format)

        # Attach handler to logger
        logger.addHandler(logfile)

        # Set logging level (INFO ignores debug logs, records INFO and above)
        logger.setLevel(logging.DEBUG)

        return logger   # Returns the configured logger instance
