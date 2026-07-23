<div align="center">

# 📦 Scapy

![Scapy](https://img.shields.io/badge/Python-Scapy-success?style=for-the-badge)

</div>

---

# 📖 Overview

Scapy is a powerful Python library used for packet creation, packet capture, packet manipulation, and network analysis.

---

# Installation

```bash
pip install scapy
```

---

# Import

```python
from scapy.all import *
```

---

# Packet Sniffing

```python
from scapy.all import sniff

sniff(count=5)
```

---

# Capture TCP Packets

```python
sniff(filter="tcp",count=10)
```

---

# Show Packet

```python
packet.show()
```

---

# Send ICMP Packet

```python
send(IP(dst="8.8.8.8")/ICMP())
```

---

# Cybersecurity Applications

- Packet Analysis
- IDS Development
- Network Monitoring
- Protocol Testing
- Traffic Analysis

---

# Best Practices

- Test only in authorized environments.
- Understand packet structures before crafting packets.
