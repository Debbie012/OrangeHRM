import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Action.Action_Page import LoginPage
from Config.configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
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



