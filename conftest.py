import os
import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--base-url", action="store", default="https://www.saucedemo.com", help="Base URL")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--window-size=1920,1080")

        drv = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)

    else:
        raise ValueError("Unsupported browser. Use --browser=chrome or --browser=firefox")

    drv.implicitly_wait(5)
    drv.set_page_load_timeout(30)

    yield drv

    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    On test failure:
      - save screenshot to reports/screenshots/
      - embed screenshot into pytest-html report (when --html is used)
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver", None)
        if not drv:
            return

        os.makedirs("reports/screenshots", exist_ok=True)

        safe_name = item.nodeid.replace("::", "__").replace("/", "_").replace("\\", "_")
        screenshot_path = os.path.join("reports", "screenshots", f"{safe_name}.png")

        drv.save_screenshot(screenshot_path)

        # Only attach if pytest-html is enabled (i.e., you're running with --html=...)
        if item.config.pluginmanager.hasplugin("html"):
            extra = getattr(rep, "extra", [])
            extra.append(extras.image(screenshot_path, name="Screenshot on Failure"))
            rep.extra = extra
