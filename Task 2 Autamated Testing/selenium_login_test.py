# Task 2: Automated Testing with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup (Make sure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Replace with the actual URL of your login page
url = "http://example.com/login"
driver.get(url)

# Define login function
def test_login(username, password):
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for response

# Test 1: Valid credentials
print("Testing valid credentials...")
test_login("valid_user", "valid_pass")

# Capture screenshot
driver.save_screenshot("valid_login_result.png")

# Test 2: Invalid credentials
print("Testing invalid credentials...")
driver.get(url)  # Reload page
test_login("invalid_user", "wrong_pass")

# Capture screenshot
driver.save_screenshot("invalid_login_result.png")

# Close browser
driver.quit()
