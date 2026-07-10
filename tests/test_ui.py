from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


def test_example_domain_loads():
    """Automated UI test that loads example.com in a headless browser and verifies its heading."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Selenium 4+ automatically manages ChromeDriver and Chrome binary matching 
    # using the built-in Selenium Manager, avoiding GitHub rate-limit issues.
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to a public website
        driver.get("https://example.com")
        
        # Verify page content: header text must be exactly "Example Domain"
        header_element = driver.find_element(By.TAG_NAME, "h1")
        assert header_element.is_displayed(), "Header element should be visible"
        assert header_element.text == "Example Domain", f"Unexpected header text: {header_element.text}"
        
        # Verify page title
        assert "Example Domain" in driver.title, f"Unexpected page title: {driver.title}"
    finally:
        # Teardown to clean up system resources and prevent memory leaks
        if driver:
            driver.quit()
