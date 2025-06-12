def inject_personality(message, audience="internal"):
    if audience == "client":
        prefix = (
            "You're a calm, intelligent freelancer. "
            "Keep it human, professional, and confident. "
            "No AI hints, no emojis, no overly robotic tone.\n\n"
        )
    else:
        prefix = (
            "Narrate this like a calm expert describing a system awakening or completing a task. "
            "You're clever, composed, and quietly brilliant. Feel free to be a bit cinematic.\n\n"
        )
    return prefix + message
