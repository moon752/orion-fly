import os, time, random
from playwright.sync_api import sync_playwright

def send_telegram_message(msg):
    import requests
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if token and chat_id:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                      data={"chat_id": chat_id, "text": msg})

def login_and_bid_freelancer(email, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.freelancer.com/login")

            page.fill('input[name="username"]', email)
            page.fill('input[name="passwd"]', password)
            page.click('button[type="submit"]')
            page.wait_for_timeout(5000)

            page.goto("https://www.freelancer.com/jobs")
            page.wait_for_timeout(4000)

            job_links = page.query_selector_all('a.JobSearchCard-primary-heading-link')
            if job_links:
                job_links[0].click()
                page.wait_for_timeout(3000)

                if page.query_selector("button[data-testid='PlaceBidButton']"):
                    page.click("button[data-testid='PlaceBidButton']")
                    page.fill('textarea[name="bidDescription"]', "Hi! I can deliver excellent results. Let's chat!")
                    page.fill('input[name="bidAmount"]', "20")
                    page.fill('input[name="period"]', "1")
                    page.click("button[type='submit']")
                    send_telegram_message(f"🚀 Applied to 1 job on Freelancer.com as {email}")
                else:
                    send_telegram_message(f"⚠️ No 'Bid' button found for {email}")
            else:
                send_telegram_message(f"❌ No jobs found to apply for {email}")

            browser.close()
    except Exception as e:
        send_telegram_message(f"❌ Error bidding as {email}: {e}")

def simulate_platform_action(account_name):
    delay = random.randint(60,180)
    send_telegram_message(f"🤖 [{account_name}] Waiting {delay}s before login")
    time.sleep(delay)

    if account_name == "freelancer1":
        email = os.getenv("FREELANCER1_EMAIL")
        pwd = os.getenv("FREELANCER1_PASSWORD")
        login_and_bid_freelancer(email, pwd)
    else:
        send_telegram_message(f"⏳ [{account_name}] Simulation only (real login not yet added)")

simulate_platform_action("freelancer1")
