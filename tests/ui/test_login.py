from src.pages.login_page import LoginPage


def test_valid_login(driver, base_url):
    login_page = LoginPage(driver)
    login_page.load(base_url)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver, base_url):
    login_page = LoginPage(driver)
    login_page.load(base_url)
    login_page.login("locked_out_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()
