import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from captcha_solver import solve_captcha  # This should exist or be injected
from conversation_layer import generate_reply  # This handles human-like replies

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # remove this line to see browser (debug only)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login_to_freelancer(email, password):
    driver = setup_driver()
    driver.get("https://www.freelancer.com/login")

    print(f"> Orion: 🔐 Logging in as {email}")
    time.sleep(3)

    try:
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        time.sleep(5)
    except NoSuchElementException:
        print("❌ Login form not found.")
        driver.quit()
        return None

    # CAPTCHA check
    if "captcha" in driver.page_source.lower():
        print("> Orion: 🧠 CAPTCHA detected. Solving...")
        solve_captcha(driver)
        time.sleep(5)

    if "dashboard" in driver.current_url:
        print("✅ Login successful!")
    else:
        print("❌ Login failed.")
    
    return driver

def check_messages_and_reply(driver):
    print("> Orion: 📬 Checking messages...")
    driver.get("https://www.freelancer.com/messages")
    time.sleep(5)

    try:
        chats = driver.find_elements(By.CSS_SELECTOR, "a[data-qa='conversation-item']")
        for chat in chats[:3]:  # Only check first 3 chats
            chat.click()
            time.sleep(3)
            last_message = driver.find_elements(By.CSS_SELECTOR, "div[data-qa='message-text']")[-1].text
            print(f"💬 Last client message: {last_message}")

            reply = generate_reply(last_message)
            msg_box = driver.find_element(By.CSS_SELECTOR, "textarea[data-qa='message-input']")
            msg_box.send_keys(reply)
            driver.find_element(By.CSS_SELECTOR, "button[data-qa='send-button']").click()
            print(f"✅ Replied: {reply}")
            time.sleep(2)
    except Exception as e:
        print(f"❌ Error while reading or replying: {e}")
    
    driver.quit()
