<div align="center">

# ⚡ Multithreading in Python

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=24&duration=3500&pause=1000&color=FFD43B&center=true&vCenter=true&width=900&lines=Run+Tasks+Concurrently;Speed+Up+Security+Tools;Efficient+Python+Programming" />

![Threading](https://img.shields.io/badge/Python-Multithreading-success?style=for-the-badge)

</div>

---

# 📖 Overview

Multithreading allows multiple tasks to execute concurrently within the same process.

It is commonly used in cybersecurity tools to improve speed and responsiveness.

---

# Why Use Threads?

- Faster Port Scanners
- Faster Network Enumeration
- Web Crawlers
- Log Processing
- API Requests

---

# Example

```python
import threading

def hello():
    print("Hello Thread")

thread = threading.Thread(target=hello)

thread.start()

thread.join()
```

---

# Thread Pool

```python
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x*x

with ThreadPoolExecutor(max_workers=5) as executor:
    print(list(executor.map(square,[1,2,3,4])))
```

---

# Best Practices

- Keep shared data synchronized.
- Avoid race conditions.
- Limit the number of worker threads.

---

# Cybersecurity Applications

- Port Scanner
- Web Enumeration
- Vulnerability Scanner
- Concurrent Requests
