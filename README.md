# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game Purpose:** The purpose of the game is for the user to guess a randomly generated secret number within a limited number of attempts. The game provides feedback after each guess, keeps track of the player's score and attempts, and tells the player whether the guess was too high, too low, or correct.

- [x] **Bugs Found:** I found several bugs while investigating the starter application. The HIGHER/LOWER hints were reversed, so a guess that was too high could tell the player to go higher. I also found that the secret number was converted between an integer and a string on alternating attempts, which caused inconsistent comparisons. I also identified an inconsistency between the displayed difficulty range and the range used when starting a new game.

- [x] **Fixes Applied:** I used AI assistance to identify and debug the problems and refactored the `check_guess()` game logic into `logic_utils.py`. I corrected the high/low behavior so the core logic returns `Too High`, `Too Low`, or `Win`, while `app.py` displays the appropriate HIGHER or LOWER message. I also removed the alternating string conversion so the secret remains an integer during comparisons. Finally, I added a pytest boundary test and used the existing starter tests to verify the refactored logic.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user starts a new game and the application generates a secret number. For this example, assume the secret number is `50`.
2. The user enters `40`. The game returns `Too Low` and the hint correctly tells the user to go `HIGHER`.
3. The user enters `60`. The game returns `Too High` and the hint correctly tells the user to go `LOWER`.
4. After each guess, the application updates the player's attempts and score while keeping the same secret number for comparison.
5. The user enters `50`. The game returns `Win`, displays the successful result, and ends the game.
6. The repaired `check_guess()` logic was also verified with pytest, including a boundary test confirming that a guess of `51` against a secret of `50` returns `Too High`.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
========================= test session starts ==========================
platform win32 -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\COD\Documents\AI110\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\COD\Documents\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 4 items                                                       
tests/test_game_logic.py::test_winning_guess PASSED               [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED              [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED               [ 75%]
tests/test_game_logic.py::test_guess_just_above_secret_is_too_high PASSED [100%]

========================== 4 passed in 1.67s ===========================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
