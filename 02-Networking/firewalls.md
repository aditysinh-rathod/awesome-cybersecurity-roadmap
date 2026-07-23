<div align="center">

# 🔥 Firewalls

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=24&duration=3500&pause=1000&color=FF4444&center=true&vCenter=true&width=900&lines=Protecting+Networks;Traffic+Filtering;Defense+in+Depth" />

![Firewall](https://img.shields.io/badge/Security-Firewall-red?style=for-the-badge)

</div>

---

# 📖 Overview

A firewall monitors and controls incoming and outgoing network traffic based on predefined security rules.

---

# Types of Firewalls

| Firewall | Description |
|----------|-------------|
| Packet Filtering | Basic Filtering |
| Stateful Inspection | Tracks Connections |
| Proxy Firewall | Acts as Intermediary |
| Next-Generation Firewall (NGFW) | Deep Packet Inspection |
| Web Application Firewall (WAF) | Protects Web Apps |

---

# How a Firewall Works

```text
Internet

↓

Firewall

↓

Allow or Block

↓

Internal Network
```

---

# Common Firewall Rules

- Allow HTTPS (443)
- Allow SSH (22) from trusted IPs
- Block Telnet (23)
- Block Unused Ports
- Restrict Remote Access

---

# Linux Firewall Commands

## UFW

```bash
sudo ufw enable

sudo ufw status

sudo ufw allow 22

sudo ufw allow 80

sudo ufw allow 443

sudo ufw deny 23
```

---

# Security Best Practices

- Default Deny Policy
- Least Privilege
- Regular Rule Reviews
- Enable Logging
- Keep Firewall Updated

---

# Cybersecurity Applications

- Prevent Unauthorized Access
- Network Segmentation
- Attack Mitigation
- Compliance Enforcement

---

# Key Takeaways

- Firewalls are the first line of defense.
- Use least-privilege rules.
- Regularly review firewall policies.
