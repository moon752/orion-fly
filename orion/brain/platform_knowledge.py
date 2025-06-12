PLATFORM_KNOWLEDGE = {
    "freelancer": {
        "max_daily_bids": 10,
        "peak_hours": ["09:00-12:00", "18:00-21:00"],
        "client_types": ["tech", "content", "data"],
    },
    "fiverr": {
        "max_daily_gigs": 7,
        "review_window": "24h",
        "client_types": ["quick-delivery", "long-term"],
    },
    "guru": {
        "max_projects": 8,
        "trusted_badge_required": False,
    },
    "workana": {
        "language_focus": "Spanish",
        "max_bids": 12,
        "client_attention_span": "short",
    }
}

def get_platform_intel(name):
    return PLATFORM_KNOWLEDGE.get(name.lower(), {})
