
import random
import time
from openrouter_client import query_ai
from telegram_reporter import notify

def choose_bid_amount(min_budget, max_budget):
    return round(random.uniform(min_budget, max_budget), 2)

def generate_proposal(description, skills):
    prompt = f"Write a human freelance proposal for the following project:\n\nDescription: {description}\n\nSkills: {skills}"
    response = query_ai(prompt)
    return response.strip()

def apply_to_job(job, account_email):
    try:
        title = job["title"]
        desc = job["description"]
        skills = job["skills"]
        budget = job["budget"]
        
        bid_amount = choose_bid_amount(budget["min"], budget["max"])
        proposal = generate_proposal(desc, skills)

        notify(f"🤖 ORION prepared bid for {title}\n💵 {bid_amount}$\n📨 {proposal[:200]}...")

        return {
            "title": title,
            "bid_amount": bid_amount,
            "proposal": proposal,
            "status": "ready"
        }
    except Exception as e:
        notify(f"❌ ORION failed to generate bid: {e}")
        return {"status": "error", "error": str(e)}

