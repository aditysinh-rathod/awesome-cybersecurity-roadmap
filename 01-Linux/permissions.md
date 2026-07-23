# 🔐 Linux File Permissions

## 📖 Overview

Linux uses file permissions to control who can read, write, or execute files.

Every file has:

- Owner
- Group
- Others

---

# Permission Types

| Symbol | Meaning |
|--------|---------|
| r | Read |
| w | Write |
| x | Execute |

---

# Example

```text
-rwxr-xr--
```

| Part | Meaning |
|------|---------|
| Owner | rwx |
| Group | r-x |
| Others | r-- |

---

# Numeric Permissions

| Number | Permission |
|---------|------------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 0 | --- |

Example:

```bash
chmod 755 file.sh
chmod 644 notes.txt
chmod +x script.sh
```

---

# Ownership

```bash
chown user file
chown user:group file
```

---

# Check Permissions

```bash
ls -l
```

---

# Best Practices

- Give minimum permissions required
- Avoid using 777
- Secure sensitive files
