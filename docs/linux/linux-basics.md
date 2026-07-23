# 🐧 Linux Basics

Welcome to the first lesson of the Linux module.

Linux is the backbone of modern cybersecurity. Most servers, cloud platforms, and security tools run on Linux.

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

- Explain what Linux is
- Understand Linux distributions
- Open and use the terminal
- Navigate the Linux file system
- Run basic commands
- Understand absolute and relative paths

---

## 📖 What is Linux?

Linux is an **open-source operating system** based on the Unix operating system.

It was created by **Linus Torvalds** in **1991**.

Today Linux powers:

- 🌐 Web Servers
- ☁️ Cloud Platforms
- 📱 Android Phones
- 💻 Supercomputers
- 🛡️ Cybersecurity Tools
- 🐳 Docker Containers
- ⚙️ DevOps Infrastructure

---

## 🏗 Linux Architecture

```text
+-----------------------+
|       User            |
+-----------------------+
|    Applications       |
+-----------------------+
|        Shell          |
+-----------------------+
|       Kernel          |
+-----------------------+
|      Hardware         |
+-----------------------+
```

### User

The person using the computer.

### Applications

Programs like Firefox, VS Code, Wireshark, Burp Suite, etc.

### Shell

The command-line interface that accepts commands.

### Kernel

The core of Linux.

It manages:

- CPU
- Memory
- Storage
- Devices
- Processes

### Hardware

Physical components like CPU, RAM, SSD, Keyboard, Mouse.

---

## 🐧 Popular Linux Distributions

| Distribution | Purpose |
|--------------|---------|
| Ubuntu | Beginner Friendly |
| Kali Linux | Penetration Testing |
| Parrot OS | Security & Privacy |
| Debian | Stable Servers |
| Fedora | Latest Features |
| Arch Linux | Advanced Users |

---

## 📂 Linux File System

Everything in Linux starts from the **root directory**.

```text
/
├── home
├── bin
├── etc
├── var
├── usr
├── opt
├── tmp
└── root
```

---

## 📁 Important Directories

| Directory | Purpose |
|------------|---------|
| / | Root directory |
| /home | User files |
| /bin | Essential commands |
| /etc | Configuration files |
| /var | Logs |
| /tmp | Temporary files |
| /usr | Installed applications |
| /root | Root user's home |

---

## 💻 First Linux Commands

### Print Working Directory

```bash
pwd
```

Example output

```text
/home/aditya
```

---

### List Files

```bash
ls
```

Detailed view

```bash
ls -l
```

Hidden files

```bash
ls -la
```

---

### Change Directory

```bash
cd Documents
```

Go back

```bash
cd ..
```

Go home

```bash
cd ~
```

Go to root

```bash
cd /
```

---

### Create Folder

```bash
mkdir CyberLab
```

---

### Create File

```bash
touch notes.txt
```

---

### Copy Files

```bash
cp notes.txt backup.txt
```

---

### Move Files

```bash
mv backup.txt Documents/
```

---

### Delete File

```bash
rm notes.txt
```

---

### Delete Folder

```bash
rm -r CyberLab
```

---

## 📌 Absolute vs Relative Path

### Absolute Path

Starts from `/`

Example

```text
/home/user/Documents/file.txt
```

### Relative Path

Starts from the current directory.

Example

```text
Documents/file.txt
```

---

## 💡 Tips

!!! tip "Remember"

    Linux commands are **case-sensitive**.

Example

```bash
Documents
```

is different from

```bash
documents
```

---

## ⚠ Common Beginner Mistakes

- Using uppercase and lowercase incorrectly
- Forgetting spaces in commands
- Accidentally deleting files with `rm -r`
- Confusing `/` with `~`

---

## 🧪 Practice Exercises

Try these commands yourself.

```bash
pwd
```

```bash
ls
```

```bash
mkdir Practice
```

```bash
cd Practice
```

```bash
touch test.txt
```

```bash
ls -la
```

```bash
cd ..
```

```bash
rm -r Practice
```

---

## ❓ Quick Quiz

### 1. What command prints the current directory?

<details>
<summary>Answer</summary>

`pwd`

</details>

---

### 2. Which directory stores configuration files?

<details>
<summary>Answer</summary>

/etc

</details>

---

### 3. Which command lists hidden files?

<details>
<summary>Answer</summary>

`ls -la`

</details>

---

### 4. Which command creates a folder?

<details>
<summary>Answer</summary>

`mkdir`

</details>

---

### 5. What does `cd ~` do?

<details>
<summary>Answer</summary>

Moves to the user's home directory.

</details>

---

## 📚 Summary

In this lesson you learned:

- ✅ What Linux is
- ✅ Linux architecture
- ✅ Linux distributions
- ✅ Linux file system
- ✅ Basic Linux commands
- ✅ Absolute and relative paths

---

## 🚀 Next Lesson

Continue learning the Linux file system.

[:material-arrow-right: Linux File System](file-system.md){ .md-button .md-button--primary }
