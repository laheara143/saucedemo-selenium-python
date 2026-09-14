from selenium.webdriver.common.by import By


def test_valid_add_to_cart(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    #Add Item
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Remove Item
    driver.find_element(By.ID, "remove-sauce-labs-backpack" ).click()

    #Add Item back
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Verify cart Updates
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")   
    assert cart_badge.text == "1"

    #Navigate to Cart
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    #Enter Checkout Info
    driver.find_element(By.ID, "first-name").send_keys('standard')
    driver.find_element(By.ID, "last-name").send_keys('user')
    driver.find_element(By.ID, "postal-code").send_keys('01111')

    #Click COntinue
    driver.find_element(By.ID, "continue").click()

    #Verify Total
    assert total.endswith("32.39") 
    
    #Checkout
    driver.find_element(By.ID, "finish").click()

    #Verify With Screenshot
    driver.save_screenshot(f"screenshots/saucedemo_{timestamp}.png")


