import string
import math
import random
# -------------------------------
# CLASS 1: Password

class Password:
    """Represents a user's password with controlled access and evaluation tools."""

    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) == 0:
            raise ValueError("Password cannot be empty")

        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def masked(self):
        return "*" * len(self._value)

    @property
    def length(self):
        return len(self._value)

    @property
    def contains_uppercase(self):
        return any(c.isupper() for c in self._value)

    @property
    def contains_lowercase(self):
        return any(c.islower() for c in self._value)

    @property
    def contains_digit(self):
        return any(c.isdigit() for c in self._value)

    @property
    def contains_special(self):
        return any(c in string.punctuation for c in self._value)

    def __str__(self):
        return f"Password(masked='{self.masked}', length={self.length})"

    def __repr__(self):
        return f"Password('{self._value}')"




# CLASS 2: PasswordPolicy

class PasswordPolicy:
    """Defines password requirements and validates a Password object."""

    def __init__(
        self,
        min_length=8,
        require_upper=True,
        require_lower=True,
        require_digit=True,
        require_special=True
    ):
        self._min_length = min_length
        self._require_upper = require_upper
        self._require_lower = require_lower
        self._require_digit = require_digit
        self._require_special = require_special

    def validate(self, password: Password) -> bool:
        if password.length < self._min_length:
            return False
        if self._require_upper and not password.contains_uppercase:
            return False
        if self._require_lower and not password.contains_lowercase:
            return False
        if self._require_digit and not password.contains_digit:
            return False
        if self._require_special and not password.contains_special:
            return False
        return True

    def __str__(self):
        return f"PasswordPolicy(min_length={self._min_length})"




# CLASS 3: PasswordAnalyzer

class PasswordAnalyzer:
    """Runs strength, entropy, pattern checks, and common-password detection."""

    COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123"]

    def __init__(self, password: Password):
        self._password = password

    def entropy(self):
        pool = 0
        if self._password.contains_lowercase:
            pool += 26
        if self._password.contains_uppercase:
            pool += 26
        if self._password.contains_digit:
            pool += 10
        if self._password.contains_special:
            pool += len(string.punctuation)

        if pool == 0:
            return 0.0
        return round(self._password.length * math.log2(pool), 2)

    def strength(self):
        score = 0
        if self._password.length >= 8:
            score += 1
        if self._password.contains_lowercase:
            score += 1
        if self._password.contains_uppercase:
            score += 1
        if self._password.contains_digit:
            score += 1
        if self._password.contains_special:
            score += 1

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        return "Strong"

    def has_repeated_patterns(self):
        pw = self._password.value
        n = len(pw)

        for size in range(1, n // 2 + 1):
            for start in range(n - 2 * size + 1):
                if pw[start:start+size] == pw[start+size:start+2*size]:
                    return True
        return False

    def is_common(self):
        return self._password.value.lower() in (p.lower() for p in self.COMMON_PASSWORDS)

    def analyze(self):
        return {
            "password": self._password.masked,
            "length": self._password.length,
            "entropy": self.entropy(),
            "strength": self.strength(),
            "is_common": self.is_common(),
            "has_repeats": self.has_repeated_patterns()
        }




# CLASS 4: PasswordGenerator

class PasswordGenerator:
    """Generates strong random passwords based on a password policy."""

    def __init__(self, policy: PasswordPolicy):
        self._policy = policy

    def generate(self, length=12):
        if length < self._policy._min_length:
            raise ValueError("Requested password length is below policy minimum")

        while True:
            chars = [
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(string.punctuation),
            ]

            remaining = length - 4
            chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining)

            random.shuffle(chars)
            password = Password("".join(chars))

            if self._policy.validate(password):
                return password



# CLASS 5: PasswordReport

class PasswordReport:
    """Formats and displays password analysis results."""

    def __init__(self, analysis_dict: dict):
        self._data = analysis_dict

    def __str__(self):
        return (
            "Password Analysis Report\n"
            "------------------------\n"
            f"Password: {self._data['password']}\n"
            f"Length: {self._data['length']}\n"
            f"Entropy: {self._data['entropy']}\n"
            f"Strength: {self._data['strength']}\n"
            f"Common Password: {self._data['is_common']}\n"
            f"Repeated Patterns: {self._data['has_repeats']}\n"
        )

    def __repr__(self):
        return f"PasswordReport({self._data})"
