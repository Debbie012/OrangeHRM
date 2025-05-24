import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Login_Page import LoginLocators
from Config.configuration import Config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(Config.WAIT_TIME)

    def open_login_page(self, url):
        self.driver.get(url)
        time.sleep(Config.WAIT_TIME)

    def username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Username))
        enter_username.send_keys(username)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Password))
        enter_password.send_keys(password)

    def submit(self):
        click_login = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Login_Button))
        click_login.click()

