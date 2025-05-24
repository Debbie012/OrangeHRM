# OrangeHRM Automation
This project automates the login feature of the OrangeHRM using Selenium with Python.

✅ Automated Feature
Login Page: Automates login using valid credentials.

# Setting up POM
Create virtual environment 
Click Python version at the bottom right of Pycharm
Click on Add New Interpreter
Click Local Interpreter
Click OK

Create a requirements.txt file
Open Pycharm Terminal
Use the Commandline below to install requirements.txt 

-pip install -r requirements.txt
-pip  freeze
-pip  freeze > requirements.txt

Use the Commandline below to Install Selenium 
pip install selenium

Use the Commandlines below to install two Python packages
pip install selenium pytest
pip install pytest-html

✅ 1. selenium
A browser automation framework.
Allows you to control web browsers through programs for testing web applications.
Often used in automated UI testing.

✅ 2. pytest
A powerful testing framework for Python.
Used for writing and running unit tests, functional tests, or even end-to-end tests.

My_Selenium_Project/
│
├── Create a Python Package - locators
│   └── Create a Python File - login_page.py
│
├──Create a Python Package - Actions 
│   └── Create Python File Actions_Page.py
│
├──Create a Python Package - Test_Script
│   └──Create a Python File - Test_Login.py
│
├── requirements.txt
└── conftest.py (for pytest setup, if using pytest)

# LocatorsPage
Create a Python Package - Config
Create a Python File - configuration

class LoginLocators:
      Input_Email = (By.CSS_SELECTOR, "input[name='username']")
      Input_Password = (By.CSS_SELECTOR, "input[name='password']")
      Login_Button = (By.CSS_SELECTOR, "button.orangehrm-login-button")

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Login_Page import LoginLocators

# ActionPage
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Email))
        enter_email_address.send_keys(email_address)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Password))
        enter_password.send_keys(password)

    def login(self):
        click_login = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Login_Button))
        click_login.click()

# Test_Script
import pytest
from selenium import webdriver

from Action.Action_Page import LoginPage
from Config.configuration import Config

@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

def test_login_page_on_orange_hrm(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.submit()

Config
class Config:
      USERNAME = "Admin"
      PASSWORD = "admin123"
      BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
      WAIT_TIME = 5