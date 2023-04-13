import pytest

import inspect
import logging
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    #tuple
    # implementing logging
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        # get object for logging feature
        logger = logging.getLogger(logger_name)  # "__name__" captures current filename which is "BaseClass"; Replaced by loggerName to display the correct testcase name into logfile.log

        # filehandler
        file_handler = logging.FileHandler('C:\\Users\\User\\PycharmProjects1\\PythonSeleniumFramework\\utilities\\logfile.log')
        # format
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # logs format
        file_handler.setFormatter(formatter)  # pass formatter to filehandler

        # clear file handler
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)  # pass filehandler object into it


        # set logger level (debug is the lowest, critical is the highest)
        logger.setLevel(logging.DEBUG)  # set level from debug to critical; Debug, info, warning, error, and critical will be shown.

        return logger

    # all reusable function should be placed here as custom utilities
    def verify_element_located(self, link_txt):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, link_txt)))

    def select_option_by_visible_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)