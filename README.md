# Password Strength Analyzer

A simple Python command-line program that classifies passwords as **weak**, **medium**, or **strong** based on length, numeric characters, and special characters.

## Features

- Accepts multiple passwords from the user
- Counts password length
- Detects numeric characters
- Detects special characters
- Classifies each password as:
  - Weak
  - Medium
  - Strong
- Tracks totals for each category
- Stores and displays weak passwords at the end

## Classification Logic

- **Weak:** fewer than 6 characters
- **Medium:** 6–9 characters
- **Strong:** 10 or more characters and contains at least one number and one special character
- Passwords with 10+ characters that do not meet the strong requirements are classified as medium

## Technologies & Concepts

- Python 3
- Loops
- Conditionals
- String processing
- Lists
- User input
- Counters and flags
- Basic input validation

## Running the Project

```bash
python3 password_strength_analyzer.py
```

The program asks how many passwords you want to test and then evaluates them one by one.

## Example

```text
Please enter the number of passwords: 3
Please enter the password: abc
Password is weak
Please enter the password: password
Password is medium
Please enter the password: Secure123!
Password is strong
```

## Bug Fixes

The original version had a logic issue where the strong-password condition could never be reached because a broader `count >= 10` branch was checked first.

The corrected version also resets the password length counter and character-detection flags for every new password.

## What I Learned

This project strengthened my understanding of conditional logic, loops, string analysis, state tracking, and debugging control-flow problems in Python.

## Author

**Ameer Daibes**  
Computer Engineering Student — Birzeit University

[LinkedIn](https://www.linkedin.com/in/ameer-daibes-1510aa207)
