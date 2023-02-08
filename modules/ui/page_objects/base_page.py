from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(
            '/Users/User/Mudryk/chromedriver.exe'))

    def close(self):
        self.driver.close()
