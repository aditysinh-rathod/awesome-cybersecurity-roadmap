# 📜 Log Analysis

## Why Logs Matter

Logs help detect attacks, troubleshoot issues, and investigate incidents.

---

# Important Log Files

| File | Purpose |
|------|---------|
| /var/log/auth.log | Authentication |
| /var/log/syslog | System logs |
| /var/log/kern.log | Kernel |
| /var/log/dmesg | Boot logs |

---

# Useful Commands

```bash
tail -f /var/log/syslog

grep "Failed" auth.log

journalctl
```

---

# Security Tips

- Monitor failed logins
- Check unusual activity
- Archive logs regularly
