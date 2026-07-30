# 🔐 Linux File Permissions

File permissions control **who can read, write, or execute files and directories**. Understanding permissions is essential for system administration and cybersecurity.

---

## 🎯 Learning Objectives

After this lesson, you will be able to:

- Understand Linux ownership
- Read file permissions
- Change permissions using `chmod`
- Change ownership using `chown`
- Understand numeric permissions
- Use symbolic permissions
- Learn about SUID, SGID, and Sticky Bit

---

# 👤 Ownership in Linux

Every file and directory has:

- Owner (User)
- Group
- Others

Example:

```text
-rwxr-xr-- 1 aditya developers 1024 Jul 30 notes.txt
```

| Part | Meaning |
|------|---------|
| aditya | Owner |
| developers | Group |
| Others | Everyone else |

---

# 📖 Reading Permissions

Example:

```text
-rwxr-xr--
```

Breakdown:

```text
- rwx r-x r--
```

| Permission | Meaning |
|------------|---------|
| r | Read |
| w | Write |
| x | Execute |

---

## Permission Groups

```text
Owner   Group   Others

rwx      r-x      r--
```

---

# 📊 Numeric Permissions

Each permission has a value.

| Permission | Value |
|------------|------:|
| Read | 4 |
| Write | 2 |
| Execute | 1 |

Examples:

| Number | Permission |
|--------|------------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 0 | --- |

---

# Common Permission Values

| Number | Meaning |
|--------|----------|
| 777 | Everyone has full access |
| 755 | Owner full, others read & execute |
| 700 | Only owner has access |
| 644 | Owner read/write, others read |
| 600 | Private file |

---

# 🔧 chmod Command

Change permissions.

Syntax

```bash
chmod PERMISSION FILE
```

Example

```bash
chmod 755 script.sh
```

Private file

```bash
chmod 600 secrets.txt
```

Executable script

```bash
chmod +x script.sh
```

Remove execute

```bash
chmod -x script.sh
```

---

# Symbolic Permissions

Grant permission

```bash
chmod u+x script.sh
```

Remove permission

```bash
chmod g-w notes.txt
```

Read only

```bash
chmod o-r file.txt
```

---

## Symbols

| Symbol | Meaning |
|--------|---------|
| u | User |
| g | Group |
| o | Others |
| a | All |

---

# 👑 chown Command

Change owner.

```bash
sudo chown alice notes.txt
```

Owner and group

```bash
sudo chown alice:developers notes.txt
```

Recursive

```bash
sudo chown -R alice Projects
```

---

# 👥 chgrp Command

Change group.

```bash
sudo chgrp developers notes.txt
```

---

# 🛡 umask

Default permissions for new files.

Check current value

```bash
umask
```

Example output

```text
0022
```

Typical defaults:

| File | Permission |
|------|------------|
| Files | 644 |
| Directories | 755 |

---

# 🚩 Special Permissions

## SUID

Run with owner's privileges.

```bash
chmod u+s program
```

Example

```text
-rwsr-xr-x
```

---

## SGID

Run with group's privileges.

```bash
chmod g+s folder
```

Example

```text
drwxr-sr-x
```

---

## Sticky Bit

Only file owner can delete files.

```bash
chmod +t shared
```

Example

```text
drwxrwxrwt
```

Common example:

```text
/tmp
```

---

# 🔍 Check Permissions

Detailed listing

```bash
ls -l
```

Example

```text
-rwxr-xr--
```

---

# 📂 Directory Permissions

| Permission | Meaning |
|------------|----------|
| r | List files |
| w | Create/Delete files |
| x | Enter directory |

---

# ⚠ Security Best Practices

✅ Give minimum permissions required.

✅ Avoid

```bash
chmod 777
```

unless absolutely necessary.

✅ Keep sensitive files private.

Example

```bash
chmod 600 id_rsa
```

---

# 🧪 Practice Lab

Complete the following tasks.

1. Create a file named `secret.txt`
2. Make it readable only by the owner.
3. Create a script named `backup.sh`
4. Make the script executable.
5. Change ownership of a folder.
6. Check permissions using `ls -l`.
7. Create a shared folder with the sticky bit.

---

# 💻 Practice Commands

```bash
touch secret.txt
```

```bash
chmod 600 secret.txt
```

```bash
touch backup.sh
```

```bash
chmod +x backup.sh
```

```bash
ls -l
```

```bash
chmod 755 backup.sh
```

```bash
chmod 644 notes.txt
```

```bash
chmod 700 private
```

```bash
chmod +t shared
```

---

# ❓ Quiz

### 1. What does permission 755 mean?

<details>
<summary>Answer</summary>

Owner has full access. Group and Others have read and execute permissions.

</details>

---

### 2. Which command makes a script executable?

<details>
<summary>Answer</summary>

```bash
chmod +x script.sh
```

</details>

---

### 3. Which command changes file ownership?

<details>
<summary>Answer</summary>

```bash
chown
```

</details>

---

### 4. What does the Sticky Bit do?

<details>
<summary>Answer</summary>

Only the owner of a file can delete it within a shared directory.

</details>

---

### 5. Why should `chmod 777` be avoided?

<details>
<summary>Answer</summary>

It grants full permissions to everyone, creating a major security risk.

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ File ownership
- ✅ Read, Write, Execute permissions
- ✅ Numeric permissions
- ✅ Symbolic permissions
- ✅ chmod
- ✅ chown
- ✅ chgrp
- ✅ umask
- ✅ SUID
- ✅ SGID
- ✅ Sticky Bit
- ✅ Security best practices

---

# 🚀 Next Lesson

Continue to **Bash Scripting**.

[:material-arrow-right: Bash Scripting](bash.md){ .md-button .md-button--primary }
