from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    def go_to(self, url):
        self.driver.get(url)

    def try_login(self, username, password):

        find_elem = self.driver.find_element(By.ID, 'login_field')
        find_elem.send_keys(username)

        find_pass = self.driver.find_element(By.ID, 'password')
        find_pass.send_keys(password)

        find_btn = self.driver.find_element(By.NAME, 'commit')
        find_btn.click()

    def check_title(self, title_name):
        return self.driver.title == title_name
