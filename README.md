# Grade Calculator

Takes marks out of 100 for four subjects, validates each input,
computes the percentage, and outputs a letter grade (A–F).

## How to run
python grade-calculator.py

## What I learned
- Input validation before computation (fail fast on bad data)
- exit() to bail early instead of nesting everything in an if
- The importance of naming: `percentage` is clearer than `grade`
  when you also output "A/B/C/D/F"

## Known limitations
- Repetition: 4 identical validation blocks. This is exactly the
  kind of code loops and functions will eliminate. Will refactor
  next week.
- No string input handling (typing "abc" raises ValueError).
