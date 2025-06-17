import re

def checkpassword(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength = strength+1
    else:
        remarks.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength = strength+1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength = strength+1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength = strength+1
    else:
        remarks.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Use at least one special character.")

    return strength, remarks

# User Interface
password = input("Enter your password to check: ")
score, feedback = checkpassword(password)

print("\nPassword Strength Report:")
if score == 5:
    print("Strong Password!")

elif 3 <= score < 5:
    print("Moderate Password.")

else:
    print("Weak Password.")

for item in feedback:
    print(item)
