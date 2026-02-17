def test_homepage_loads(driver, base_url):
    driver.get(base_url)
    assert "Swag Labs" in driver.title

