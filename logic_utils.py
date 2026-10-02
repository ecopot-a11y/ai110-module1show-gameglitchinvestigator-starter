def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: Refactored parse_guess into logic_utils.py after AI-assisted edge-case testing.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    try:
        guess_int = int(float(raw))
        return True, guess_int, None
    except (ValueError, TypeError):
        return False, None, "Please enter a valid number."
    
# FIX: Refactored check_guess logic into logic_utils.py with AI assistance.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"

    if guess > secret:
        return "Too High"

    return "Too Low"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
