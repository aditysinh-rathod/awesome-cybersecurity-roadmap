# 🌱 Environment Variables

## Overview

Environment variables store configuration values securely outside your code.

---

## Why Use Them?

- Hide API Keys
- Store Secrets
- Separate Development & Production
- Improve Security

---

## Python Example

```python
import os

api_key = os.getenv("API_KEY")

print(api_key)
```

---

## Linux

```bash
export API_KEY="your_key"
```

---

## .env Example

```text
API_KEY=123456
SECRET_KEY=mysecret
```

---

## Load .env

```python
from dotenv import load_dotenv

load_dotenv()
```

---

## Install

```bash
pip install python-dotenv
```

---

## Best Practices

- Never commit `.env` files.
- Add `.env` to `.gitignore`.
- Rotate secrets regularly.
