import re
import string



def is_non_empty(password: str) -> bool:
    """Check if the password is non-empty.

    Args:
        password (str): Password to check.

    Returns:
        bool: True if password is not empty, False otherwise.

    Raises:
        TypeError: If password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return len(password) > 0



def has_min_length(password: str, min_length: int = 8) -> bool:
    """Check if password meets minimum length requirement.

    Args:
        password (str): Password to check.
        min_length (int): Minimum length required.

    Returns:
        bool: True if password length >= min_length, False otherwise.

    Raises:
        TypeError: If password is not a string or min_length is not an int.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if not isinstance(min_length, int):
        raise TypeError("Minimum length must be an integer")
    return len(password) >= min_length



def contains_uppercase(password: str) -> bool:
    """Check if password contains at least one uppercase letter."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return any(c.isupper() for c in password)



def contains_lowercase(password: str) -> bool:
    """Check if password contains at least one lowercase letter."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return any(c.islower() for c in password)



def contains_digit(password: str) -> bool:
    """Check if password contains at least one digit."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return any(c.isdigit() for c in password)



def contains_special_char(password: str) -> bool:
    """Check if password contains at least one special character."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    special_chars = string.punctuation
    return any(c in special_chars for c in password)



def calculate_entropy(password: str) -> float:
    """Estimate the entropy (strength) of a password based on character sets.

    Args:
        password (str): Password to evaluate.

    Returns:
        float: Approximate entropy value.

    Raises:
        TypeError: If password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    pool = 0
    if contains_lowercase(password):
        pool += 26
    if contains_uppercase(password):
        pool += 26
    if contains_digit(password):
        pool += 10
    if contains_special_char(password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0.0
    import math
    return round(len(password) * math.log2(pool), 2)



def check_password_strength(password: str) -> str:
    """Categorize password as Weak, Medium, or Strong.

    Args:
        password (str): Password to evaluate.

    Returns:
        str: Strength category.
    """
    if not is_non_empty(password):
        return "Invalid"
    score = 0
    if has_min_length(password):
        score += 1
    if contains_uppercase(password):
        score += 1
    if contains_lowercase(password):
        score += 1
    if contains_digit(password):
        score += 1
    if contains_special_char(password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"



def count_character_types(password: str) -> dict:
    """Return a dictionary with counts of letters, digits, and special chars.

    Args:
        password (str): Password to evaluate.

    Returns:
        dict: Counts of 'uppercase', 'lowercase', 'digits', 'special'.
    """
    counts = {"uppercase": 0, "lowercase": 0, "digits": 0, "special": 0}
    for c in password:
        if c.isupper():
            counts["uppercase"] += 1
        elif c.islower():
            counts["lowercase"] += 1
        elif c.isdigit():
            counts["digits"] += 1
        elif c in string.punctuation:
            counts["special"] += 1
    return counts



def is_common_password(password: str, common_list: list = None) -> bool:
    """Check if password is in a list of common passwords.

    Args:
        password (str): Password to check.
        common_list (list): Optional list of common passwords.

    Returns:
        bool: True if password is common, False otherwise.
    """
    if common_list is None:
        # Minimal example list
        common_list = ["password", "123456", "qwerty", "abc123"]
    return password.lower() in (p.lower() for p in common_list)



def mask_password(password: str) -> str:
    """Return a masked version of the password (for UI display).

    Args:
        password (str): Password to mask.

    Returns:
        str: Masked password with asterisks.
    """
    return '*' * len(password)



def generate_strong_password(length: int = 12) -> str:
    """Generate a random strong password containing letters, digits, and special chars.

    Args:
        length (int): Desired length of password.

    Returns:
        str: Generated strong password.

    Raises:
        ValueError: If length < 8
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    import random

    while True:
        password_chars = []
        password_chars.append(random.choice(string.ascii_uppercase))
        password_chars.append(random.choice(string.ascii_lowercase))
        password_chars.append(random.choice(string.digits))
        password_chars.append(random.choice(string.punctuation))

        remaining_length = length - 4
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password_chars += random.choices(all_chars, k=remaining_length)
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        if check_password_strength(password) == "Strong":
            return password



def detect_repeated_patterns(password: str) -> bool:
    """Detect if a password contains repeated patterns like 'abcabc' or '1212'.

    Args:
        password (str): Password to check.

    Returns:
        bool: True if repeated patterns exist, False otherwise.
    """
    n = len(password)
    for size in range(1, n // 2 + 1):
        for start in range(n - 2 * size + 1):
            if password[start:start + size] == password[start + size:start + 2 * size]:
                return True
    return False



def advanced_password_evaluation(password: str) -> dict:
    """Perform a detailed evaluation including entropy, strength, common checks, and patterns.

    Args:
        password (str): Password to evaluate.

    Returns:
        dict: Evaluation summary.
    """
    evaluation = {
        "length": len(password),
        "counts": count_character_types(password),
        "entropy": calculate_entropy(password),
        "strength": check_password_strength(password),
        "is_common": is_common_password(password),
        "has_repeats": detect_repeated_patterns(password),
        "masked": mask_password(password)
    }
    return evaluation



if __name__ == "__main__":
    test_passwords = ["password123!", "Abc$1234", "aaAA11!!", "", "StrongPass#2025"]
    for pwd in test_passwords:
        print(f"Evaluating password: {pwd}")
        result = advanced_password_evaluation(pwd)
        for k, v in result.items():
            print(f"  {k}: {v}")
        print("-" * 50)
