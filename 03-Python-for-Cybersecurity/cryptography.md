# 🛡 Cryptography

## Overview

Cryptography protects information using encryption and decryption.

---

# Concepts

- Encryption
- Decryption
- Keys
- Certificates
- Digital Signatures

---

# Symmetric Encryption

- AES
- DES

---

# Asymmetric Encryption

- RSA
- ECC

---

# Python Example

```python
from cryptography.fernet import Fernet

key=Fernet.generate_key()

cipher=Fernet(key)

encrypted=cipher.encrypt(b"Hello")

print(encrypted)
```

---

# Install

```bash
pip install cryptography
```

---

# Applications

- Secure Storage
- Secure Communication
- Certificates
- HTTPS
