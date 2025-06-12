from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()

    def get_error_message(self):
        return self.driver.find_element(By.ID, "error").text
