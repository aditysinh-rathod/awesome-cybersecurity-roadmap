<div align="center">

# 🌐 Domain Name System (DNS)

![DNS](https://img.shields.io/badge/Networking-DNS-orange?style=for-the-badge)

</div>

---

# 📖 Overview

DNS translates domain names into IP addresses.

Example:

```text
google.com
↓

142.250.xxx.xxx
```

---

# DNS Resolution Process

```text
User

↓

Browser Cache

↓

Operating System Cache

↓

Recursive Resolver

↓

Root Server

↓

TLD Server

↓

Authoritative DNS

↓

IP Address Returned
```

---

# DNS Record Types

| Record | Purpose |
|---------|----------|
| A | IPv4 |
| AAAA | IPv6 |
| CNAME | Alias |
| MX | Mail Server |
| TXT | Verification |
| NS | Name Server |

---

# Commands

```bash
nslookup google.com

dig google.com

host google.com
```

---

# Security Risks

- DNS Spoofing
- Cache Poisoning
- DNS Tunneling
- Domain Hijacking

---

# Best Practices

- Use DNSSEC where available
- Monitor DNS traffic
- Use trusted DNS resolvers
