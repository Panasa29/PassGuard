
import getpass


# Check password length
def check_length(pw):
    length = len(pw)

    if length >= 12:
        return 3
    elif length >= 8:
        return 2
    else:
        return 0


# Check lowercase letters
def check_lowercase(pw):
    if any(c.islower() for c in pw):
        return 1
    else:
        return 0


# Check uppercase letters
def check_uppercase(pw):
    if any(c.isupper() for c in pw):
        return 1
    else:
        return 0


# Check digits
def check_digit(pw):
    if any(c.isdigit() for c in pw):
        return 1
    else:
        return 0


# Check special symbols
def check_symbol(pw):
    if any(not c.isalnum() for c in pw):
        return 1
    else:
        return 0


# Calculate total score
def calculate_score(pw):
    score = 0

    score += check_length(pw)
    score += check_lowercase(pw)
    score += check_uppercase(pw)
    score += check_digit(pw)
    score += check_symbol(pw)

    return score


# Identify password strength
def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 5:
        return "Medium"
    else:
        return "Strong"


# Generate improvement tips
def get_tips(pw):
    tips = []

    if len(pw) < 12:
        tips.append("Use at least 12 characters.")

    if not any(c.islower() for c in pw):
        tips.append("Add at least one lowercase letter.")

    if not any(c.isupper() for c in pw):
        tips.append("Add at least one uppercase letter.")

    if not any(c.isdigit() for c in pw):
        tips.append("Add at least one number.")

    if not any(not c.isalnum() for c in pw):
        tips.append("Add at least one special symbol.")

    return tips


# Main program
print("=" * 35)
print("       PASSGUARD")
print("   PASSWORD STRENGTH CHECKER")
print("=" * 35)

password = getpass.getpass("Enter a sample password: ")

score = calculate_score(password)
strength = get_strength(score)
tips = get_tips(password)

print("\n========== RESULTS ==========")
print("Password Score:", score, "/ 7")
print("Password Strength:", strength)

if tips:
    print("\nImprovement Suggestions:")

    for tip in tips:
        print("-", tip)
else:
    print("\nAll basic checks passed!")

print("\nThank you for using PassGuard!")
password = getpass.getpass("Enter a sample password: ")

score = calculate_score(password)
strength = get_strength(score)
tips = get_tips(password)