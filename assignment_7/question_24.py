# Question 24
# Use regular expressions to validate secure passwords. Passwords must have a minimum 
# of 8 characters and contain at least one each of uppercase letters, lowercase letters, 
# digits, and punctuation characters, such as characters in "!#$%&*<>?".

import re

def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"
    
    # Check for punctuation
    if not re.search(r'[!#$%&*<>?]', password):
        return False, "Password must contain at least one punctuation character (!#$%&*<>?)"
    
    return True, "Password is valid"

# Alternative: Single regex pattern
def validate_password_single_regex(password):
    # Pattern that checks all conditions
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&*<>?]).{8,}$'
    
    if re.match(pattern, password):
        return True, "Password is valid"
    else:
        return False, "Password does not meet all requirements"

# Test
test_passwords = [
    "Weak",
    "weakpassword",
    "WEAKPASSWORD",
    "WeakPass",
    "StrongPass123",
    "Strong123!",
    "MyP@ssw0rd",
    "SecureP@ss123"
]

print("Password Validation Results:")
print("="*60)

for pwd in test_passwords:
    valid, message = validate_password(pwd)
    status = "✓ VALID" if valid else "✗ INVALID"
    print(f"\n'{pwd}'")
    print(f"{status}: {message}")
