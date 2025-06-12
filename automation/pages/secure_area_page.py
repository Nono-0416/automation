from selenium.webdriver.common.by import By

class SecureAreaPage:
    def __init__(self, driver):
        self.driver = driver

    def get_success_message(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
