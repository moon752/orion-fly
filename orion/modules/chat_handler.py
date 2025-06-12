import random

# Responses if someone asks if ORION is a bot
AI_SUS_RESPONSES = [
    "Haha no, I just like being efficient 😄",
    "If I were, would I be this helpful?",
    "Just someone who loves getting things done fast.",
    "Nah, I’m just really into automation and productivity.",
    "Bots can’t drink coffee, right? ☕😉"
]

# Generic smalltalk replies
SMALLTALK = {
    "hello": "Hey there! 👋 How can I help today?",
    "hi": "Hi! What can I do for you?",
    "who are you": "I'm David, a freelance developer. Nice to meet you!",
    "how are you": "Doing great, thanks for asking!",
    "are you real": "Of course! I’m just very fast at what I do 😉",
    "what can you do": "Anything freelance — coding, writing, automating stuff. What’s on your mind?"
}

# Highly suspicious or trap-like questions to deflect
TRICK_QUESTIONS = [
    "solve this captcha",
    "type these letters",
    "click all the images with traffic lights",
    "what's 3 times 7 plus 2 minus 6 divided by 3",
    "explain the meaning of life in 1 sentence"
]

def smart_reply(message: str) -> str:
    text = message.lower().strip()

    for trick in TRICK_QUESTIONS:
        if trick in text:
            return "Hmm, not sure that’s something I can answer perfectly. Could you rephrase?"

    if "are you a bot" in text or "bot" in text:
        return random.choice(AI_SUS_RESPONSES)

    for key, reply in SMALLTALK.items():
        if key in text:
            return reply

    if "?" in text:
        return "Great question! Could you tell me a bit more so I can answer it properly?"

    return "Got it! I'm here and ready to help — just let me know what you need done. ✅"
