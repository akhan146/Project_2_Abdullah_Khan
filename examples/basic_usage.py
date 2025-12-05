import sys
import os

# Allow Python to find the src/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.library_item import (
    Password,
    PasswordPolicy,
    PasswordAnalyzer,
    PasswordGenerator,
    PasswordReport
)

pw = Password("Abc$1234")
policy = PasswordPolicy(min_length=8)

analyzer = PasswordAnalyzer(pw)
results = analyzer.analyze()

report = PasswordReport(results)
print(report)

# Generate strong password
generator = PasswordGenerator(policy)
new_pw = generator.generate(12)
print("Generated:", new_pw)
