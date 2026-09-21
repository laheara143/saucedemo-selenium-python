from selenium.webdriver.common.by import By


def test_remove_from_cart(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    #Add Item
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Verify cart Updates
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")   
    assert cart_badge.text == "1"

    #Remove Item
    driver.find_element(By.ID, "remove-sauce-labs-backpack" ).click()

    driver.save_screenshot(f"1screenshots/debug_saucedemo.png")

    #Verify cart Updates
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")   
    assert cart_badge.text == "1"

    #Verify With Screenshot
    driver.save_screenshot(f"screenshots/saucedemo_{timestamp}.png")


