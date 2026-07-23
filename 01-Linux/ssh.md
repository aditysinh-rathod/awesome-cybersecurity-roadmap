# 🔑 Secure Shell (SSH)

## 📖 Overview

SSH allows secure remote access to Linux systems using encrypted communication.

---

# Connect

```bash
ssh user@192.168.1.10
```

---

# Generate SSH Keys

```bash
ssh-keygen
```

---

# Copy Key

```bash
ssh-copy-id user@server
```

---

# Transfer Files

```bash
scp file.txt user@server:/home/user
```

---

# Best Practices

- Disable root login
- Use SSH keys
- Disable password authentication
- Change default port
- Enable firewall
