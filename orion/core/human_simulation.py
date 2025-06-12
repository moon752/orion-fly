import random
import time

def human_delay(min_seconds=4, max_seconds=12):
    delay = random.uniform(min_seconds, max_seconds)
    print(f"[HUMAN SIMULATION] Waiting {delay:.2f}s before acting...")
    time.sleep(delay)

def generate_human_name():
    names = ["David Muigai", "Aisha Khan", "Miguel Torres", "Samantha Leigh", "Elias Morgan"]
    return random.choice(names)

def type_like_human(text, min_delay=0.03, max_delay=0.15):
    output = ""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(min_delay, max_delay))
        output += char
    return output

def cover_letter_template(job_title, name):
    return f"""
Hi there,

I'm excited about your {job_title} project. I've completed similar tasks and would love to help you succeed.

Looking forward to hearing from you!

Thanks,  
{name}
"""
