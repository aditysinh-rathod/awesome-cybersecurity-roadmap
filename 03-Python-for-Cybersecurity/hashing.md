# 🔐 Hashing

## Overview

Hashing converts data into a fixed-length value.

Hashes are one-way and cannot be reversed.

---

# Common Algorithms

| Algorithm | Size |
|------------|------|
| MD5 | 128-bit |
| SHA1 | 160-bit |
| SHA256 | 256-bit |
| SHA512 | 512-bit |

---

# Example

```python
import hashlib

text="Cyber"

hash=hashlib.sha256(text.encode())

print(hash.hexdigest())
```

---

# Verify Hash

```python
hashlib.sha256(file.read()).hexdigest()
```

---

# Cybersecurity Uses

- Password Storage
- File Integrity
- Malware Detection
- Digital Evidence
