import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(client_msg, platform="freelancer"):
    prompt = f"You are a top freelancer. A client on {platform} says: '{client_msg}'. Respond professionally and close the deal."
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message['content']
