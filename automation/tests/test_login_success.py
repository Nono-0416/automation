import pytest
from pages.login_page import LoginPage
from utils import save_screenshot
from pages.secure_area_page import SecureAreaPage

@pytest.mark.order(1)
def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("student", "Password123")

    secure_page = SecureAreaPage(browser)
    assert secure_page.get_success_message() == "Logged In Successfully"
    save_screenshot(browser,"login_success")

