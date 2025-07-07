import time
import pytest
from utils import save_screenshot
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.order(3)
@pytest.mark.parametrize("username, password, expected_error", 
[("invalid_user", "Password123", "Your username is invalid!"),
("student", "wrongpass", "Your password is invalid!")])
def test_login_failures(browser, username, password, expected_error):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(username, password)
    time.sleep(2)
    # 捲動畫面到錯誤訊息位置
    error_elem = browser.find_element(By.ID, "error")
    browser.execute_script("arguments[0].scrollIntoView(false);", error_elem)
    time.sleep(2)
    assert login_page.get_error_message() == expected_error
    save_screenshot(browser,"login_failure",)

    # def test_login_failure(browser):
    # #帳號錯誤
    # login_page = LoginPage(browser)
    # login_page.load()
    # login_page.login("invalid_user", "Password123")
    # time.sleep(1)
    # assert "Your username is invalid!" in login_page.get_error_message()
    # save_screenshot(browser,"invalid_username")

    # time.sleep(3)
    # #密碼錯誤
    # login_page = LoginPage(browser)
    # login_page.load()
    # login_page.login("student", "invalid_password")
    # time.sleep(1)
    # assert "Your password is invalid!" in login_page.get_error_message()
    # save_screenshot(browser,"invalid_password")