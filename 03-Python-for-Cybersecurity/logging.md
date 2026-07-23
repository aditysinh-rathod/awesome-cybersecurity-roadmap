# 📝 Logging

## Overview

Logging records application events, making debugging and incident investigation easier.

---

## Basic Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Program Started")
logging.warning("Warning Message")
logging.error("Error Message")
```

---

## Log Levels

| Level | Purpose |
|---------|---------|
| DEBUG | Development |
| INFO | General Information |
| WARNING | Potential Problems |
| ERROR | Errors |
| CRITICAL | Critical Failures |

---

## Cybersecurity Uses

- Audit Logs
- Intrusion Detection
- Incident Response
- Tool Debugging
