from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    """The class contains basic operations for working with the browser."""
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(
            '/Users/User/Mudryk/chromedriver.exe'))

    def close(self):
        """The method closes the open browser."""
        self.driver.close()
