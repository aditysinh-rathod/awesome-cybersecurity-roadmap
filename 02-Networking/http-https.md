<div align="center">

# 🌍 HTTP & HTTPS

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=24&duration=3500&pause=1000&color=00C8FF&center=true&vCenter=true&width=900&lines=Understanding+HTTP+and+HTTPS;Secure+Web+Communication;Foundation+of+Web+Security" />

![HTTP](https://img.shields.io/badge/Protocol-HTTP%20%7C%20HTTPS-red?style=for-the-badge)

</div>

---

# 📖 Overview

HTTP (**HyperText Transfer Protocol**) is the protocol used for communication between web browsers and web servers.

HTTPS is the secure version of HTTP that encrypts data using **SSL/TLS**.

---

# Communication Flow

```text
Browser
    │
    ▼
HTTP Request
    │
    ▼
Web Server
    │
    ▼
HTTP Response
    │
    ▼
Browser
```

---

# HTTP vs HTTPS

| HTTP | HTTPS |
|------|-------|
| Port 80 | Port 443 |
| Unencrypted | Encrypted |
| Less Secure | Secure |
| Faster | Slightly Slower |
| Vulnerable to MITM | Protected using TLS |

---

# HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update resource |
| PATCH | Partial update |
| DELETE | Delete resource |
| HEAD | Headers only |
| OPTIONS | Supported methods |

---

# Common Status Codes

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 301 | Redirect |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# HTTPS Handshake

```text
Client

↓

Client Hello

↓

Server Hello

↓

Certificate Exchange

↓

Key Exchange

↓

Encrypted Communication
```

---

# Security Risks

- Man-in-the-Middle (MITM)
- Session Hijacking
- SSL Stripping
- Insecure Cookies

---

# Best Practices

- Always use HTTPS
- Enable HSTS
- Use Secure Cookies
- Validate Certificates
- Disable Weak TLS Versions

---

# Key Takeaways

- HTTP transfers web data.
- HTTPS encrypts communication.
- HTTPS is essential for modern web security.
