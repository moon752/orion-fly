from selenium.webdriver.common.by import By
import time
from orion.brain.driver import get_driver
from orion.secret_data import freelancer, fiverr, guru, workana

def login_freelancer(email, password):
    driver = get_driver()
    driver.get("https://www.freelancer.com/login")
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "next").click()
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login").click()
    time.sleep(5)
    driver.quit()

def login_fiverr(email, password):
    driver = get_driver()
    driver.get("https://www.fiverr.com/login")
    time.sleep(3)
    driver.find_element(By.NAME, "login[email]").send_keys(email)
    driver.find_element(By.NAME, "login[password]").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    driver.quit()

def login_guru(email, password):
    driver = get_driver()
    driver.get("https://www.guru.com/login.aspx")
    time.sleep(3)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtUser").send_keys(email)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPass").send_keys(password)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnLogin").click()
    time.sleep(5)
    driver.quit()

def login_workana(email, password):
    driver = get_driver()
    driver.get("https://www.workana.com/login")
    time.sleep(3)
    driver.find_element(By.ID, "user_email").send_keys(email)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    time.sleep(5)
    driver.quit()

def run_all_logins():
    login_freelancer(freelancer["email"], freelancer["password"])
    login_fiverr(fiverr["email"], fiverr["password"])
    login_guru(guru["email"], guru["password"])
    login_workana(workana["email"], workana["password"])

if __name__ == "__main__":
    run_all_logins()

from orion.brain.stealth_utils import human_delay, retry_on_exception

@retry_on_exception(Exception)
def login_freelancer(email, password):
    driver = get_driver()
    driver.get("https://www.freelancer.com/login")
    human_delay()
    driver.find_element("name", "username").send_keys(email)
    human_delay()
    driver.find_element("name", "passwd").send_keys(password)
    human_delay()
    driver.find_element("name", "submit").click()
    human_delay(5, 8)
    driver.quit()
