# 🔍 Regular Expressions

## Overview

Regular Expressions (Regex) are patterns used to search, extract, and validate text.

---

# Import

```python
import re
```

---

# Search

```python
import re

text="User logged in"

result=re.search("User",text)
```

---

# Find All

```python
re.findall(r"\d+","Port 80 Port 443")
```

Output

```text
80
443
```

---

# Email Validation

```python
pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
```

---

# IP Address Pattern

```python
r"\d+\.\d+\.\d+\.\d+"
```

---

# Cybersecurity Uses

- Log Parsing
- IOC Extraction
- Email Validation
- URL Detection
- Threat Hunting
