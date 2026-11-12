import getpass

def check_password(password):
    checks = {
        "At least 12 characters": len(password) >= 12,
        "An uppercase letter": any(char.isupper() for char in password),
        "A lowercase letter": any(char.islower() for char in password),
        "A number": any(char.isdigit() for char in password),
        "A special character": any(not char.isalnum() for char in password),
    }

    passed = sum(checks.values())

    if all(checks.values()):
        strength = "Strong"
    elif len(password) >= 8 and passed >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\nPassword strength: {strength}")

    missing = [rule for rule, passed_check in checks.items() if not passed_check]
    if missing:
        print("To improve it:")
        for rule in missing:
            print(f"- Add/use {rule.lower()}.")
    else:
        print("Good! It meets all the checks.")


password = getpass.getpass("Enter a sample password: ")
check_password(password)
