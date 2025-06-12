import pytest
from pages.login_page import LoginPage
from utils import save_screenshot
from pages.secure_area_page import SecureAreaPage

@pytest.mark.order(3)
def test_logout(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("student", "Password123")

    secure_page = SecureAreaPage(browser)
    secure_page.logout()
    assert browser.title == "Test Login | Practice Test Automation"
    save_screenshot(browser,"logout")

