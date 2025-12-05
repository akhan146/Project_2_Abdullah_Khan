# Project 2 — Object-Oriented Password Security System  
**Author:** Abdullah Khan  
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

