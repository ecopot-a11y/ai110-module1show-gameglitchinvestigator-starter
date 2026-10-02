# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

## Challenge 1: Advanced Edge-Case Testing

### Prompt Used

> Generate a suite of pytest cases for three edge cases in my Streamlit number guessing game. Test a negative number, a decimal input, and an extremely large number using the existing `parse_guess()` and `check_guess()` functions. Keep the tests simple and consistent with the current behavior of the application.

### Edge Cases

- **Negative number (`-5`)** — Chosen to verify that numeric input outside the normal game range can be parsed without crashing the application.
- **Decimal (`40.5`)** — Chosen to verify how `parse_guess()` handles numeric input that is not already a whole number.
- **Extremely large number (`999999999`)** — Chosen to verify that the comparison logic still correctly identifies a value far above the secret as `Too High`.

### Verification

The first edge-case test run exposed an unfinished refactor because `parse_guess()` in `logic_utils.py` still raised `NotImplementedError`. After completing the `parse_guess()` refactor, I reran the complete test suite. All seven tests passed, including the three new edge-case tests.