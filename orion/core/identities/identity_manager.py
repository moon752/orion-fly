import random

IDENTITIES = {
    "freelancer": [
        {
            "name": "David Muigai",
            "bio": "AI & automation expert with 5+ years experience.",
            "avatar": "orion/assets/avatars/david.jpg"
        },
        {
            "name": "Aisha Khan",
            "bio": "Python automation engineer & data expert.",
            "avatar": "orion/assets/avatars/aisha.png"
        }
    ],
    "upwork": [
        {
            "name": "Samantha Leigh",
            "bio": "Professional writer & editor with a sharp eye for detail.",
            "avatar": "orion/assets/avatars/samantha.png"
        }
    ]
}

def get_random_identity(platform):
    return random.choice(IDENTITIES.get(platform, []))
