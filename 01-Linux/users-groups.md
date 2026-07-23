# 👥 Users and Groups

## 📖 Overview

Linux supports multiple users and groups for secure access control.

---

# User Types

| Type | Description |
|------|-------------|
| Root | Administrator |
| Normal User | Standard account |
| System User | Used by services |

---

# Useful Commands

Create user

```bash
sudo adduser john
```

Delete user

```bash
sudo userdel john
```

Change password

```bash
passwd john
```

Create group

```bash
sudo groupadd developers
```

Add user to group

```bash
sudo usermod -aG developers john
```

Check current user

```bash
whoami
```

List users

```bash
cat /etc/passwd
```

---

# Important Files

| File | Purpose |
|------|---------|
| /etc/passwd | User accounts |
| /etc/shadow | Password hashes |
| /etc/group | Group information |

---

# Security Tips

- Never work as root unless necessary
- Use strong passwords
- Apply least privilege
