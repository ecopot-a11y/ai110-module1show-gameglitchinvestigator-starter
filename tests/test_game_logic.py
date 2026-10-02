from logic_utils import check_guess, parse_guess 

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_just_above_secret_is_too_high():
    result = check_guess(51, 50)

    assert result == "Too High"

def test_negative_number_is_parsed():
    ok, guess, err = parse_guess("-5")

    assert ok is True
    assert guess == -5
    assert err is None

def test_decimal_input_is_handled():
    ok, guess, err = parse_guess("40.5")

    assert ok is True
    assert guess == 40
    assert err is None

def test_extremely_large_guess_is_too_high():
    result = check_guess(999999999, 50)

    assert result == "Too High"