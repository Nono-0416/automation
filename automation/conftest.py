import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture
# def browser(request):
#     browser_name = request.config.getoption("--browser")

#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")

#     driver.maximize_window()
#     yield driver
#     driver.quit()


# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# @pytest.fixture(params=["chrome", "firefox"])
# def browser(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {request.param}")

#     driver.maximize_window()
#     yield driver
#     driver.quit()