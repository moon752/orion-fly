import random

def generate_reply(message):
    message = message.lower()
    # Simple smart logic for now
    if "hello" in message or "hi" in message:
        return random.choice([
            "Hello! How can I assist you today?",
            "Hi there! Ready to get started on your project.",
            "Hey! Let me know what you need help with."
        ])
    elif "can you" in message or "are you able" in message:
        return random.choice([
            "Absolutely! I can take care of that.",
            "Yes, I’m fully capable of handling this task.",
            "Definitely. Let’s get to work!"
        ])
    elif "price" in message or "cost" in message:
        return random.choice([
            "My typical rate is flexible depending on the project scope.",
            "Let’s discuss a fair rate based on the requirements.",
            "I usually charge competitively — what budget do you have in mind?"
        ])
    elif "thanks" in message or "thank you" in message:
        return random.choice([
            "You’re welcome! I’m here whenever you need me.",
            "No problem at all!",
            "Glad to help!"
        ])
    else:
        return random.choice([
            "Sure, I’ll get started right away.",
            "Okay! I’ve got it.",
            "Let me handle that for you.",
            "Sounds good, I’m on it."
        ])
