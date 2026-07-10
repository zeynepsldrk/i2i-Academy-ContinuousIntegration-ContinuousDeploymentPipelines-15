from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_example_domain_loads():
    """Automated UI test that loads example.com in a headless browser and verifies its heading."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = None
    try:
        # Try to use webdriver-manager to set up ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        # Fallback to system ChromeDriver (necessary in Docker container environments)
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as fallback_err:
            raise RuntimeError(
                f"Failed to initialize Chrome WebDriver. Original error: {e}. Fallback error: {fallback_err}"
            )

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
