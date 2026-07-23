<div align="center">

# 🔌 Ports & Protocols

![Ports](https://img.shields.io/badge/Common-Ports-success?style=for-the-badge)

</div>

---

# 📖 Overview

A **port** identifies a specific service running on a device.

Protocols define how data is transmitted.

---

# Common Ports

| Port | Service |
|------|----------|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 161 | SNMP |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

---

# TCP vs UDP

| TCP | UDP |
|-----|-----|
| Reliable | Faster |
| Ordered | Unordered |
| Connection Oriented | Connectionless |

---

# Check Open Ports

```bash
ss -tuln

netstat -tuln

nmap localhost
```

---

# Security Tips

- Disable unused ports
- Restrict access with firewalls
- Monitor exposed services
- Keep services updated
