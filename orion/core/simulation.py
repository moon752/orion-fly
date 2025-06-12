def simulate_proposal(proposal_text):
    # Simple heuristic checks, NLP sanity, etc
    if len(proposal_text) < 50:
        return False, "Proposal too short"
    # Add other simulations or mocks
    return True, "Simulation passed"
