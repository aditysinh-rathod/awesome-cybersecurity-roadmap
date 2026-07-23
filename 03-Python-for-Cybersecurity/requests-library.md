# 🌍 Requests Library

## Overview

The `requests` library simplifies making HTTP requests in Python.

---

## Installation

```bash
pip install requests
```

---

## GET Request

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

---

## POST Request

```python
import requests

data = {"username": "admin"}

response = requests.post("https://example.com/login", data=data)
```

---

## JSON Response

```python
print(response.json())
```

---

## Common Methods

| Method | Purpose |
|--------|---------|
| GET | Retrieve data |
| POST | Submit data |
| PUT | Update |
| DELETE | Remove |

---

# Cybersecurity Applications

- API testing
- Security automation
- Threat intelligence
- Web reconnaissance
