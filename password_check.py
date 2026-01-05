import re

def check_password_strength(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


if __name__ == "__main__":
    user_password = input("Enter your password: ")

    if check_password_strength(user_password):
        print("✅ Password is STRONG")
    else:
        print("❌ Password is WEAK")
        print("Password must contain:")
        print("- At least 8 characters")
        print("- Uppercase and lowercase letters")
        print("- At least one digit")
        print("- At least one special character")
