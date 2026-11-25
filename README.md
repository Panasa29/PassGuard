# PassGuard – Password Strength Checker

## About the Project

PassGuard is a beginner-friendly Python cybersecurity project that evaluates password strength.

It checks password length and character variety, calculates a score, identifies the strength level, and provides suggestions to improve weak passwords.

This project runs locally on the user's computer and uses hidden password input to protect the password from being displayed while typing.

## Project Objective

The objective is to understand basic password security concepts and Python programming through a practical cybersecurity application.

## Features

- Checks password length.
- Detects lowercase letters.
- Detects uppercase letters.
- Detects numeric digits.
- Detects special symbols.
- Calculates a password strength score.
- Classifies passwords as Weak, Medium, or Strong.
- Provides suggestions to improve password strength.
- Uses Python's `getpass` module for hidden password input.
- Runs locally through the command line.

## Technologies Used

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code
- **Python Module:** getpass
- **Environment:** Python Virtual Environment
- **Operating System:** Windows

## Installation and Usage

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd PassGuard
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Run the program

```bash
python passguard.py
```

Follow the prompt to enter a sample password.

## Password Scoring System

PassGuard evaluates passwords using five basic checks.

| Check | Score |
|---|---:|
| Length of 12 or more characters | 3 |
| Length of 8–11 characters | 2 |
| Lowercase letter | 1 |
| Uppercase letter | 1 |
| Number | 1 |
| Special symbol | 1 |

### Strength Classification

- **Weak:** 0–2 points
- **Medium:** 3–5 points
- **Strong:** 6–7 points

Note: This is a basic educational scoring system, not a guarantee of password security.

## Ethical and Legal Disclaimer

PassGuard is developed strictly for educational and learning purposes.

- The program evaluates passwords entered locally by the user.
- Only use sample passwords or passwords you own.
- Never test passwords belonging to others without explicit permission.
- Do not use this project for unauthorised access or malicious activities.
- The program does not store or display the entered password.

## Author
Developed as a beginner-level Python cybersecurity project.