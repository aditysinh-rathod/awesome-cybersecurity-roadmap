<div align="center">

# 🎯 Subnetting

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=24&duration=3500&pause=1000&color=00C8FF&center=true&vCenter=true&width=900&lines=Learn+Subnetting+Step+by+Step;Divide+Networks+Efficiently;Essential+Skill+for+Cybersecurity" />

![Subnetting](https://img.shields.io/badge/Networking-Subnetting-blue?style=for-the-badge)

</div>

---

# 📖 Overview

Subnetting divides a large network into smaller, manageable networks called **subnets**.

Benefits:

- Better performance
- Better security
- Easier management
- Reduced broadcast traffic

---

# CIDR Notation

| CIDR | Subnet Mask | Hosts |
|------|-------------|-------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |

---

# Example

```text
Network: 192.168.1.0/24

Subnet 1
192.168.1.0/25

Subnet 2
192.168.1.128/25
```

---

# Useful Commands

```bash
ip addr

ip route
```

---

# Cybersecurity Use Cases

- Network Segmentation
- VLAN Design
- Firewall Rules
- Access Control

---

# Key Takeaways

- Smaller networks improve security.
- CIDR replaces traditional classful networking.
- Network segmentation limits attack spread.
