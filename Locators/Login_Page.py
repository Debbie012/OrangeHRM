from selenium.webdriver.common.by import By


class LoginLocators:
      Input_Username = (By.CSS_SELECTOR, "input[name='username']")
      Input_Password = (By.CSS_SELECTOR, "input[name='password']")
      Login_Button = (By.CSS_SELECTOR, "button.orangehrm-login-button")
