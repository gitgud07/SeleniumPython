from datetime import datetime

import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# declare driver globally to None so driver in setup function is the same as the driver from the _capture_screenshot function
driver = None
parent_dir = None

# Note: Use conftest only when you think that fixture can be used across multiple testcases
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )


# setup scope to class level to execute once per run
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # invoke Chrome browser
        #chrome_driver_path = "C:\\PythonSeleniumWebDrivers\\chromedriver.exe"
        chrome_driver_path = "C:\\Users\\User\\PycharmProjects1\\PythonSeleniumFramework\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)


    elif browser_name == "firefox":
        # invoke Firefox browser
        #firefox_driver_path = "C:\\PythonSeleniumWebDrivers\\geckodriver.exe"
        firefox_driver_path = "C:\\Users\\User\\PycharmProjects1\\PythonSeleniumFramework\\geckodriver.exe"
        firefox_binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        service_obj = Service(firefox_driver_path)
        option = webdriver.FirefoxOptions()
        option.binary_location = firefox_binary_path

        driver = webdriver.Firefox(service=service_obj, options=option)


    elif browser_name == "edge":
        # invoke Edge browser
        # edge_driver_path = "C:\\PythonSeleniumWebDrivers\\msedgedriver.exe"
        edge_driver_path = "C:\\Users\\User\\PycharmProjects1\\PythonSeleniumFramework\\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_driver_path)

    # go to this url
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # wait for 2 seconds
    driver.implicitly_wait(2)

    #maximize window
    driver.maximize_window()

    # assigning this local driver of this fixture to the class driver
    request.cls.driver = driver

    # close browser after finishing the execution
    yield
    driver.close()


#implementing screenshot in html-report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    parent_dir = os.path.dirname(os.getcwd())

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "reports/" + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)

            if file_name:
                html = (
                        '<div><img src="%s/tests/%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % (parent_dir, file_name)

                )

                extra.append(pytest_html.extras.html(html))

        report.extra = extra


# screenshot capture on failure
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# directory
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    parent_dir = os.path.dirname(os.getcwd())

    if not os.path.exists("{}\\tests\\reports".format(parent_dir)):
        os.makedirs("{}\\tests\\reports".format(parent_dir))
    config.option.htmlpath = (
            "reports/" + datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".html"
    )