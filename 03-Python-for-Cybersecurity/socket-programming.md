<div align="center">

# 🔌 Socket Programming

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=24&duration=3500&pause=1000&color=FFD43B&center=true&vCenter=true&width=900&lines=Communicate+Over+Networks;Build+TCP+and+UDP+Applications;Foundation+for+Network+Security+Tools" />

![Sockets](https://img.shields.io/badge/Python-Sockets-blue?style=for-the-badge&logo=python)

</div>

---

# 📖 Overview

A socket is one endpoint of a communication channel between two devices.

Socket programming is used to build:

- Port Scanners
- Chat Applications
- Web Servers
- Banner Grabbers
- Reverse Shells (for authorized security testing only)
- Network Monitoring Tools

---

# TCP Client

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("example.com",80))

client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

print(client.recv(1024).decode())

client.close()
```

---

# TCP Server

```python
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("0.0.0.0",8080))

server.listen()

print("Listening...")

client,address = server.accept()

print(address)
```

---

# Common Methods

| Method | Purpose |
|---------|----------|
| socket() | Create Socket |
| bind() | Bind Address |
| listen() | Wait for Connections |
| accept() | Accept Client |
| connect() | Connect Server |
| send() | Send Data |
| recv() | Receive Data |
| close() | Close Socket |

---

# Cybersecurity Applications

- Port Scanner
- Banner Grabber
- Network Monitoring
- Service Enumeration
- Custom Security Tools

---

# Key Takeaways

- TCP is reliable.
- UDP is faster.
- Socket programming is fundamental for security tool development.
