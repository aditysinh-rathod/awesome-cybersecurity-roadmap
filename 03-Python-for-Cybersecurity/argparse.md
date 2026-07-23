# ⚙️ Argparse

## Overview

Argparse allows Python scripts to accept command-line arguments.

---

## Example

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t","--target",required=True)

args = parser.parse_args()

print(args.target)
```

---

## Run

```bash
python scanner.py --target 192.168.1.1
```

---

## Benefits

- Professional CLI
- Easy Automation
- User-Friendly Tools

---

## Cybersecurity Applications

- Port Scanner
- Hash Generator
- Network Scanner
- Password Checker
