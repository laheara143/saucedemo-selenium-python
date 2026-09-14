from datetime import datetime


def test_open_saucedemo(driver):

    driver.get("https://www.saucedemo.com")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    driver.save_screenshot(f"screenshots/saucedemo_{timestamp}.png")

    assert "Swag Labs" in driver.title