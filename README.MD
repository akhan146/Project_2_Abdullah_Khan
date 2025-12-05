# Project 2 — Object-Oriented Password Security System  
**Author/Developer:** Abdullah Khan  
**Course:** INST326  

## Project Overview  
Project 2 transforms my **Project 1 password function library** into a fully object-oriented system using 5 core classes:

- `Password`
- `PasswordPolicy`
- `PasswordAnalyzer`
- `PasswordGenerator`
- `PasswordReport`

The goal of Project 2 is to demonstrate how OOP organizes related data and behaviors into reusable, modular components with encapsulation, validation, and clear responsibilities. This system prepares the foundation for **inheritance and subclassing** in Project 3.

---

## Github Repositroy Structure

```
C:.
│   .gitignore
│   LICENSE
│   README.MD
│
├───docs
│       api_reference.md
│       class_design.md
│
├───examples
│       basic_usage.py
│
└───src
    │   library.functions.py
    │   library_item.py
    │   member.py
    │
    └───loan.py

---

## 🧠 Object-Oriented Design Summary

### ✔ 1. Encapsulation  
All sensitive data (like raw password strings) is stored in **private attributes**:

```python
self._value
```

Public access is controlled through **properties**:

```python
@property
def masked(self):
    return "*" * len(self._value)
```

This prevents accidental modification and protects sensitive information.

---

### ✔ 2. Validation  
Classes validate input during initialization:

- Empty passwords → rejected  
- Policies enforce strength requirements  
- Generator ensures passwords follow policy rules  

---

### ✔ 3. Clear Responsibilities

| Class | Responsibility |

**Password**: Holds password data + exposes features like length, character types.
**PasswordPolicy**: Defines rules for what makes a password valid.
**PasswordAnalyzer**: Computes entropy, strength, common checks, and repeated patterns.
**PasswordGenerator**: Creates strong passwords following a policy.
**PasswordReport**: Formats the results in a readable report.

This matches OOP principles of **single responsibility** and **clean separation of concerns**.

---

## Cloning the Repo

### **1. Install Python**
Ensure Python 3.10+ is installed on your system.

### **2. Clone or download the repository**
```
git clone https://github.com/akhan146/Project_2_Abdullah_Khan.git
```



## Example Usage

### **basic_usage.py**

```python
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

generator = PasswordGenerator(policy)
new_pw = generator.generate(12)
print("Generated:", new_pw)
```

### **Sample Output**

```
Password Analysis Report
------------------------
Password: ********
Length: 8
Entropy: 52.44
Strength: Strong
Common Password: False
Repeated Patterns: False

Generated: Password(masked='************', length=12)
```

---

## 🏗 Class Breakdown

### Password
Encapsulates the password string and provides:

- `length`
- `masked`
- character type checks (uppercase, lowercase, digits, special)

### PasswordPolicy
Represents rules including:

- minimum length  
- requires uppercase  
- requires digits  
- requires special characters  

### PasswordAnalyzer
Applies advanced security analysis:

- entropy calculation  
- strength scoring  
- repeated pattern detection  
- common password detection  

### PasswordGenerator
Creates strong passwords that meet the policy:

- Uses randomness  
- Ensures at least one of each required character type  
- Verifies password meets policy before returning  

### PasswordReport
Pretty-prints results into a professional report format.

---

## How This Prepares for Project 3

This design supports **inheritance**, because each class has:

- clean responsibilities  
- private attributes  
- override-friendly methods  
- documented behavior  

Examples of future subclasses include:

- `UserPassword(Password)`  
- `StrictPasswordPolicy(PasswordPolicy)`  
- `JSONPasswordReport(PasswordReport)`  

The system is structured to extend naturally without rewriting existing code.

---

## Conclusion

This OOP system demonstrates:

- Encapsulation  
- Data hiding  
- Validation  
- Reusable methods  
- Modular organization  
- Real-world password security architecture  

It builds on Project 1 and creates a strong base for Project 3.

---

