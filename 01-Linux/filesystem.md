# 📂 Linux File System

## 📖 Overview

The Linux file system follows a hierarchical directory structure where everything begins at the **root directory (`/`)**.

Unlike Windows, Linux does not use drive letters (C:, D:, etc.). Every file and device exists under a single directory tree.

---

# 🗂 Linux Directory Structure

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

# 📁 Important Directories

| Directory | Purpose |
|-----------|---------|
| `/` | Root directory |
| `/home` | User home folders |
| `/root` | Root user home |
| `/etc` | Configuration files |
| `/bin` | Essential commands |
| `/usr` | User applications |
| `/var` | Logs & variable data |
| `/tmp` | Temporary files |
| `/boot` | Bootloader files |
| `/dev` | Device files |
| `/proc` | Process information |

---

# 💻 Useful Commands

```bash
pwd
ls
ls -la
tree
cd
find
du -sh
```

---

# 🎯 Key Takeaways

- Everything starts from `/`
- Linux uses a hierarchical file system
- Configuration files are stored in `/etc`
- User data is stored in `/home`
