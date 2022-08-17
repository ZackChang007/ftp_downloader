"""
/Users/admin/Documents/GitHub/ftp_downloader/Drivers/chromedriver  --remote-debugging-port=9515 --user-data-dir="/Users/admin/Documents/GitHub/ftp_downloader/cache";
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
#
# service = ChromeService(executable_path=ChromeDriverManager().install())
# print(service.path)

chrome_options = Options()
# chrome_options.binary_location = r"/Users/admin/Documents/GitHub/ftp_downloader/Drivers/chromedriver"
# chrome_options.headless = True
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
chrome_options.debugger_address = "127.0.0.1:9515"
# chrome_options.add_argument(r'--user-data-dir=/Users/admin/Documents/GitHub/ftp_downloader/cache')
print(f"{chrome_options.arguments} \n {chrome_options.binary_location} \n {chrome_options.experimental_options} \n"
      f"{chrome_options.debugger_address} \n {chrome_options.default_capabilities} \n {chrome_options.capabilities}")
# chrome_driver = r"/Users/admin/Documents/GitHub/ftp_downloader/Drivers/chromedriver"
driver = webdriver.Chrome(options=chrome_options)  # service=service,


def test_login_free():
    driver.get("https://www.baidu.com/")
    driver.implicitly_wait(5)
    print(driver.current_url)
    print(driver.title)


if __name__ == "__main__":
    test_login_free()


