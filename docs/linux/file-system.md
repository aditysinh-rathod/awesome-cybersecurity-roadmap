# 📂 Linux File System

The Linux file system organizes everything as files and directories. Understanding its structure is essential for system administration, scripting, and cybersecurity.

---

## 🎯 Learning Objectives

After this lesson, you will be able to:

- Understand the Linux directory hierarchy
- Identify common system directories
- Work with files and folders
- Understand file types
- Use symbolic and hard links
- Check disk usage

---

# 🏗 Linux Directory Structure

Everything starts from the **Root Directory**.

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

# 📖 Important Directories

| Directory | Description |
|------------|-------------|
| / | Root directory |
| /home | User home folders |
| /root | Root user's home |
| /etc | Configuration files |
| /bin | Essential commands |
| /sbin | System administration commands |
| /usr | Installed applications |
| /var | Logs and variable data |
| /tmp | Temporary files |
| /dev | Device files |
| /proc | Process information |
| /boot | Boot loader files |
| /opt | Optional software |

---

# 📁 Navigating Directories

Current directory

```bash
pwd
```

List files

```bash
ls
```

Detailed list

```bash
ls -l
```

Hidden files

```bash
ls -la
```

Change directory

```bash
cd Documents
```

Go back

```bash
cd ..
```

Go to home

```bash
cd ~
```

Go to root

```bash
cd /
```

---

# 📄 Creating Files

Create a file

```bash
touch notes.txt
```

Create multiple files

```bash
touch file1.txt file2.txt file3.txt
```

---

# 📁 Creating Directories

```bash
mkdir CyberLab
```

Nested folders

```bash
mkdir -p Projects/Linux/Basics
```

---

# 📋 Copy Files

Copy one file

```bash
cp notes.txt backup.txt
```

Copy folder

```bash
cp -r CyberLab Backup
```

---

# 🚚 Move Files

Rename

```bash
mv notes.txt linux-notes.txt
```

Move file

```bash
mv linux-notes.txt Documents/
```

---

# 🗑 Delete Files

Delete file

```bash
rm file.txt
```

Delete directory

```bash
rm -r CyberLab
```

Force delete

```bash
rm -rf CyberLab
```

> ⚠️ Be extremely careful with `rm -rf`. It permanently deletes files without asking for confirmation.

---

# 🔍 Find Files

Search by name

```bash
find . -name notes.txt
```

Search from root

```bash
find / -name "*.log"
```

---

# 🔎 Locate Files

```bash
locate firefox
```

Update database

```bash
sudo updatedb
```

---

# 📖 View File Content

Display entire file

```bash
cat notes.txt
```

First 10 lines

```bash
head notes.txt
```

Last 10 lines

```bash
tail notes.txt
```

View page by page

```bash
less notes.txt
```

---

# 📊 Check Disk Usage

Filesystem usage

```bash
df -h
```

Directory size

```bash
du -sh Documents
```

---

# 📌 File Types

Linux supports different file types.

| Symbol | File Type |
|--------|-----------|
| - | Regular File |
| d | Directory |
| l | Symbolic Link |
| c | Character Device |
| b | Block Device |
| p | Named Pipe |
| s | Socket |

Check using

```bash
ls -l
```

Example

```text
drwxr-xr-x Documents
-rw-r--r-- notes.txt
lrwxrwxrwx shortcut
```

---

# 🔗 Hard Link

Create

```bash
ln notes.txt notes-hard
```

Both files point to the same data on disk.

---

# 🔗 Symbolic Link

Create

```bash
ln -s notes.txt shortcut
```

A symbolic link acts like a shortcut.

---

# 📂 Absolute Path

Starts from root.

Example

```text
/home/aditya/Documents/file.txt
```

---

# 📂 Relative Path

Starts from the current directory.

Example

```text
Documents/file.txt
```

---

# 💡 Useful Commands

Show calendar

```bash
cal
```

Current date

```bash
date
```

Current user

```bash
whoami
```

Current logged-in users

```bash
who
```

Hostname

```bash
hostname
```

System information

```bash
uname -a
```

---

# 🧪 Practice Lab

Complete these tasks.

1. Create a folder named `CyberPractice`
2. Create three text files inside it.
3. Rename one file.
4. Copy another file.
5. Delete one file.
6. Create a symbolic link.
7. Display disk usage.
8. Find one file using `find`.

---

# ❓ Quiz

### 1. Which directory stores configuration files?

<details>
<summary>Answer</summary>

`/etc`

</details>

---

### 2. Which command shows disk usage?

<details>
<summary>Answer</summary>

```bash
df -h
```

</details>

---

### 3. Which command creates a symbolic link?

<details>
<summary>Answer</summary>

```bash
ln -s
```

</details>

---

### 4. Which command deletes a folder recursively?

<details>
<summary>Answer</summary>

```bash
rm -r
```

</details>

---

### 5. Which command searches for files?

<details>
<summary>Answer</summary>

```bash
find
```

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ Linux directory hierarchy
- ✅ File management
- ✅ Directory management
- ✅ File searching
- ✅ Disk usage
- ✅ File types
- ✅ Hard links
- ✅ Symbolic links

---

# 🚀 Next Lesson

Continue to **Linux Permissions**.

[:material-arrow-right: Linux Permissions](permissions.md){ .md-button .md-button--primary }
