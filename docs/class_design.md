# Class Design Documentation  
**Project 2 — Object-Oriented Password Security System**  
**Author:** Abdullah Khan  

## Overview  
This document explains the architectural design choices behind the object-oriented system used to analyze, validate, and generate passwords. The project extends the procedural code from Project 1 by organizing related functionality into cohesive, reusable classes.

The system is built around **five core classes**:

- `Password`
- `PasswordPolicy`
- `PasswordAnalyzer`
- `PasswordGenerator`
- `PasswordReport`

The purpose of this document is to show why each class exists, how they interact, and how the design prepares for inheritance in Project 3.

---

# Class Responsibilities & Architecture

---
# 1. `Password` — Data Encapsulation  
**Role:** Stores and protects raw password values.  
**Why a class:** The password itself is a real-world object with properties.

### Key Responsibilities:
- Store the password string in a **private attribute** (`_value`)  
- Provide **read-only access** to sensitive data  
- Compute properties such as:
  - character types  
  - masked version  
  - length  

### Why this design?
- Prevents accidental modification  
- Adds security by never exposing raw password unless needed  
- Allows future specialization (`UserPassword`, `AdminPassword`) in Project 3  

---

### 2. `PasswordPolicy` — Rule Definition  
Role: Defines what a “valid” password must include.

### Key Responsibilities:
- Minimum length requirement  
- Requirements for uppercase, lowercase, digits, special chars  
- Validate a `Password` object  

### Why this design?
- Separates rules from the password itself  
- Makes it possible to create new rules via inheritance later  
  (e.g., `StrictPolicy`, `PinPolicy`)  

---

## ### 3. `PasswordAnalyzer` — Evaluation Engine  
Role:Performs advanced analysis work.

### Responsibilities:
- Entropy calculation  
- Strength scoring  
- Repeated pattern detection  
- Common password detection  
- Produce full evaluation results  

### Why this design?
Analysis is a separate responsibility.  
We avoid mixing analysis with storage or policy checking.

---

### 4. `PasswordGenerator` — Secure Random Generator  
**Role:** Creates strong passwords that follow a policy.

### Responsibilities:
- Generate random characters  
- Guarantee compliance with `PasswordPolicy`  
- Return a ready-to-use `Password` object  

### Why this design?
Encapsulation of generation logic makes the system easier to extend, test, and replace.

---

### 5. `PasswordReport` — Formatted Output  
Role: Convert analysis results into readable text.

### Responsibilities:
- Accept analysis dictionary  
- Output formatted multi-line report  
- Prepare display-ready summary  

### Why this design?
Separating reporting from analysis allows flexible output formats later:

- JSON  
- HTML  
- PDF  
(Useful for Project 3 inheritance.)

---

# Class Interactions

```
Password → analyzed by → PasswordAnalyzer
Password → validated by → PasswordPolicy
PasswordPolicy → used by → PasswordGenerator
PasswordAnalyzer → outputs → PasswordReport
```

This architecture maintains clean boundaries between:

- **Data** (Password)  
- **Rules** (Policy)  
- **Analysis** (Analyzer)  
- **Creation** (Generator)  
- **Display** (Report)  

---

# Preparation for Project 3 (Inheritance)

This system was intentionally designed for clean subclassing:

{Base Class}                          {Possible Subclass }
| `Password`|                   | `UserPassword`, `EncryptedPassword` |
| `PasswordPolicy`|     | `StrictPasswordPolicy`, `ParentalControlPolicy` |
| `PasswordReport`|               | `JSONReport`, `PDFReport` |
| `PasswordGenerator`|     | `MnemonicGenerator`, `PINGenerator` |

Because each class has a **single responsibility**, extending the system won’t break existing behavior.

---

# Conclusion  
This architecture follows strong OOP principles:

- Encapsulation  
- Modularity  
- Separation of concerns  
- Extendability  
- Preparation for inheritance  



