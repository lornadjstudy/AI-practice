# AI Practice

My hands-on AI learning journey, one small project at a time.

## Week 1: Python and JSON basics

What I built:
- A years_of_service function with a Senior/Mid-level check
- An employee list saved to and read from a JSON file
- Filters by department and status

What I learned:
- Indentation decides what belongs inside a loop or an if
- dump/load work with files, dumps/loads work with strings

What broke:
- Used the wrong variable name inside my function (fixed it)
- Colab could not save, so I copied my code to GitHub by hand
Click Commit changes..., then Commit changes again.
---
## Week 2: APIs and my first LLM call

What I built:
- Called the GitHub API with Python requests
- A script that asks Gemini a typed question and saves the answers to a log file
- try/except with raise_for_status so errors show a friendly message

What I learned:
- 404 = wrong place, 400 = wrong message, 401/403 = wrong key
- Keep API keys in Colab Secrets, never in code or GitHub
- The answer is nested inside the JSON: candidates, content, parts, text

What broke:
- Code got pasted into the secret's value box, so the "key" was wrong
- Used textwrap.fill on the whole response instead of just the answer text
- Left except without "as e", so the error message could not print

