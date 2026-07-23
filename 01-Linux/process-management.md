# ⚙️ Process Management

## 📖 Overview

A process is a running instance of a program.

Understanding processes is essential for system administration and incident response.

---

# Important Commands

| Command | Description |
|---------|-------------|
| ps | List processes |
| top | Real-time monitoring |
| htop | Interactive monitoring |
| kill | Stop process |
| killall | Stop multiple processes |
| jobs | Background jobs |
| bg | Resume in background |
| fg | Bring to foreground |

---

# Examples

```bash
ps aux

top

kill 1234

kill -9 1234
```

---

# Process States

- Running
- Sleeping
- Zombie
- Stopped

---

# Security Tips

- Monitor unknown processes
- Kill malicious processes
- Check resource usage regularly
