from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_post_message():
    # Set up WebDriver
    service = Service(r"C:\Users\himan\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to the application
        driver.get("http://localhost:5000")

        # Login to the application
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.NAME, "username").send_keys("himani")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        # Wait for the homepage to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Find the "Say Something" text area and enter a message
        message_field = driver.find_element(By.ID, "post")  # Using ID 'post'
        message_field.send_keys("This is a test post!")  # Your test message

        # Locate the Submit button and click it
        submit_button = driver.find_element(By.ID, "submit")  # Using ID 'submit'
        submit_button.click()

        # Wait for the new post to appear on the feed
        post = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'This is a test post!')]"))
        )

        # Verify the post is displayed on the feed
        assert "This is a test post!" in post.text
        print("Test Passed: Post successfully added to the feed.")
    finally:
        driver.quit()
