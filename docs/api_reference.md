# API Reference  
**Object-Oriented Password Security System**  
**Author:** Abdullah Khan  

This document provides detailed reference-level documentation for each class, method, and property in the system.

---

# 📘 Class: `Password`

### **Purpose**
Stores password data securely with controlled access.

### **Initialization**
```python
Password(value: str)
```

### **Properties**
| Property | Description |
|----------|-------------|
| `value` | Raw password (read-only) |
| `masked` | Returns "*"-masked password |
| `length` | Number of characters |
| `contains_uppercase` | True if at least one uppercase letter |
| `contains_lowercase` | True if at least one lowercase |
| `contains_digit` | True if at least one digit |
| `contains_special` | True if at least one symbol |

---

# 📘 Class: `PasswordPolicy`

### **Purpose**
Defines rules for what makes a password acceptable.

### **Initialization**
```python
PasswordPolicy(
    min_length=8,
    require_upper=True,
    require_lower=True,
    require_digit=True,
    require_special=True
)
```

### **Method**
| Method | Description |
|--------|-------------|
| `validate(password)` | Returns True if the password satisfies the policy |

---

# 📘 Class: `PasswordAnalyzer`

### **Purpose**
Performs evaluations on a `Password` object.

### **Initialization**
```python
PasswordAnalyzer(password: Password)
```

### **Methods**
| Method | Description |
|--------|-------------|
| `entropy()` | Calculates entropy of the password |
| `strength()` | Returns “Weak”, “Medium”, or “Strong” |
| `has_repeated_patterns()` | Detects repeated substring sequences |
| `is_common()` | Checks common password list |
| `analyze()` | Returns full analysis dictionary |

---

# 📘 Class: `PasswordGenerator`

### **Purpose**
Generates random strong passwords that follow policy rules.

### **Initialization**
```python
PasswordGenerator(policy: PasswordPolicy)
```

### **Method**
| Method | Description |
|--------|-------------|
| `generate(length=12)` | Returns a new `Password` object that meets policy requirements |

---

# 📘 Class: `PasswordReport`

### **Purpose**
Formats analysis results into readable output.

### **Initialization**
```python
PasswordReport(analysis_dict: dict)
```

### Methods
                | Method |            | Description |

                | `__str__()`|        | Returns formatted multi-line report |
                | `__repr__()`|       | Debug representation |

---

# Summary Table

| Class |               | Key Role |

| `Password` |          | Secure storage + properties |
| `PasswordPolicy` |    | Validation rules |
| `PasswordAnalyzer`|   | Full evaluation engine |
| `PasswordGenerator`|  | Creates compliant passwords |
| `PasswordReport`|     | Formats analysis |



