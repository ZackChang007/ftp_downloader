# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""
Most machines automatically update the browser, but the driver does not.
To make sure you get the correct driver for your browser,
there are many third party libraries to assist you.
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Use install() to get the location used by the manager and pass it into service class
service = ChromeService(executable_path=ChromeDriverManager().install())
print(service.path)
# Use Service instance when initializing the driver:
driver = webdriver.Chrome(service=service)


# # https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_install_drivers.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.ie.service import Service as IEService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.microsoft import IEDriverManager
#
#
# def test_driver_manager_chrome():
#     service = ChromeService(executable_path=ChromeDriverManager().install())
#
#     driver = webdriver.Chrome(service=service)
#
#     driver.quit()
#
#
# def test_edge_session():
#     service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
#
#     driver = webdriver.Edge(service=service)
#
#     driver.quit()
#
#
# def test_firefox_session():
#     service = FirefoxService(executable_path=GeckoDriverManager().install())
#
#     driver = webdriver.Firefox(service=service)
#
#     driver.quit()
#
#
# @pytest.mark.skip(reason="only runs on Windows")
# def test_ie_session():
#     service = IEService(executable_path=IEDriverManager().install())
#
#     driver = webdriver.Ie(service=service)
#
#     driver.quit()