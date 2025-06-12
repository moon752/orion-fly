import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

EMAIL = os.getenv("FREELANCER_EMAIL")
PASSWORD = os.getenv("FREELANCER_PASSWORD")

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login(driver):
    driver.get("https://www.freelancer.com/login")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys(EMAIL)
    driver.find_element(By.NAME, "passwd").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

def main():
    driver = setup_driver()
    login(driver)
    print("🟢 ORION Logged in successfully.")
    # More job logic goes here...
    driver.quit()

if __name__ == "__main__":
    main()
