from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_login():
    # Set up WebDriver
    service = Service(r"C:\Users\himan\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to the application
        driver.get("http://localhost:5000")  # Replace with your app's URL

        # Navigate to Login Page
        driver.find_element(By.LINK_TEXT, "Login").click()

        # Enter Login Credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys("himani")  # Update with correct username
        password_field.send_keys("123")    # Update with correct password
        password_field.send_keys(Keys.RETURN)

        # Wait for the post-login page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Check the welcome message
        welcome_message = driver.find_element(By.TAG_NAME, "h1").text
        assert "Hi, himani!" in welcome_message  # Update expected text

        print("Test Passed: Login successful and welcome message displayed.")
    finally:
        driver.quit()
