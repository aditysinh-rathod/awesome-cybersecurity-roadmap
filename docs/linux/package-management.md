# 📦 Linux Package Management

Package management is the process of installing, updating, removing, and managing software on a Linux system.

Every Linux distribution uses a package manager to simplify software installation and dependency management.

---

# 🎯 Learning Objectives

After completing this lesson, you will be able to:

- Understand package management
- Install software
- Update packages
- Remove packages
- Search repositories
- Understand dependencies
- Use APT, DNF, YUM, and Pacman

---

# 🤔 What is a Package?

A package is a compressed file containing:

- Program files
- Libraries
- Configuration files
- Documentation
- Dependencies

Examples:

- Google Chrome
- Python
- Git
- Nmap
- Wireshark

---

# 📦 Popular Package Managers

| Distribution | Package Manager |
|--------------|-----------------|
| Ubuntu | APT |
| Debian | APT |
| Kali Linux | APT |
| Fedora | DNF |
| RHEL | YUM / DNF |
| CentOS | YUM |
| Arch Linux | Pacman |

---

# 🔄 Update Package List

Ubuntu / Debian

```bash
sudo apt update
```

This downloads the latest package information.

---

# ⬆ Upgrade Installed Packages

```bash
sudo apt upgrade
```

Upgrade everything

```bash
sudo apt full-upgrade
```

---

# 📥 Install Software

Example:

```bash
sudo apt install git
```

Install multiple packages

```bash
sudo apt install git curl wget
```

---

# 🗑 Remove Software

Remove package

```bash
sudo apt remove git
```

Remove including configuration

```bash
sudo apt purge git
```

---

# 🧹 Remove Unused Packages

```bash
sudo apt autoremove
```

Clean downloaded package cache

```bash
sudo apt clean
```

---

# 🔍 Search Packages

```bash
apt search wireshark
```

Show package information

```bash
apt show git
```

---

# 📋 List Installed Packages

```bash
apt list --installed
```

---

# 📦 Install Local Package

Install a downloaded `.deb` file

```bash
sudo dpkg -i package.deb
```

Fix dependency issues

```bash
sudo apt install -f
```

---

# 🔗 Package Dependencies

Many applications depend on other packages.

Example:

```text
Wireshark
      │
      ├── libpcap
      ├── Qt
      ├── GLib
      └── GTK
```

APT automatically installs required dependencies.

---

# 📂 Repository

A repository is an online collection of software packages.

Examples:

- Ubuntu Repository
- Debian Repository
- Kali Repository

Repository list:

```bash
cat /etc/apt/sources.list
```

---

# 📦 DNF Commands (Fedora)

Update

```bash
sudo dnf update
```

Install

```bash
sudo dnf install git
```

Remove

```bash
sudo dnf remove git
```

---

# 📦 YUM Commands (CentOS)

Install

```bash
sudo yum install git
```

Update

```bash
sudo yum update
```

---

# 📦 Pacman Commands (Arch Linux)

Update

```bash
sudo pacman -Syu
```

Install

```bash
sudo pacman -S git
```

Remove

```bash
sudo pacman -R git
```

---

# 🔐 Security Best Practices

✅ Install software from trusted repositories.

✅ Keep packages updated.

✅ Remove unused packages.

✅ Avoid downloading unknown `.deb` or `.rpm` files.

---

# ⚠ Common Mistakes

❌ Forgetting to run

```bash
sudo apt update
```

before installing.

❌ Mixing package managers.

❌ Installing software from untrusted sources.

---

# 🧪 Practice Lab

Complete these tasks.

1. Update package lists.
2. Upgrade installed packages.
3. Install Git.
4. Install Curl.
5. Search for Wireshark.
6. Remove Curl.
7. Clean package cache.

---

# 💻 Practice Commands

Update

```bash
sudo apt update
```

Upgrade

```bash
sudo apt upgrade
```

Install Git

```bash
sudo apt install git
```

Search

```bash
apt search python
```

Show details

```bash
apt show git
```

Remove

```bash
sudo apt remove git
```

Autoremove

```bash
sudo apt autoremove
```

---

# ❓ Quiz

### 1. Which command updates package information?

<details>
<summary>Answer</summary>

```bash
sudo apt update
```

</details>

---

### 2. Which command installs Git?

<details>
<summary>Answer</summary>

```bash
sudo apt install git
```

</details>

---

### 3. Which command removes unused packages?

<details>
<summary>Answer</summary>

```bash
sudo apt autoremove
```

</details>

---

### 4. Which command searches repositories?

<details>
<summary>Answer</summary>

```bash
apt search
```

</details>

---

### 5. What is a repository?

<details>
<summary>Answer</summary>

A repository is an online collection of software packages that can be installed and updated using a package manager.

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ Package managers
- ✅ Installing software
- ✅ Updating packages
- ✅ Removing packages
- ✅ Searching repositories
- ✅ Dependencies
- ✅ Security best practices

---

# 🚀 Next Lesson

Continue to **Linux Networking Commands**.

[:material-arrow-right: Networking Commands](networking-commands.md){ .md-button .md-button--primary }
