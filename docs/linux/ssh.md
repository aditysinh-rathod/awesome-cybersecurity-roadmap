# 🔐 SSH (Secure Shell)

SSH (Secure Shell) is a secure network protocol used to remotely access and manage Linux systems over an encrypted connection. It is one of the most important tools for Linux administrators, DevOps engineers, cloud engineers, and cybersecurity professionals.

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

- Understand what SSH is
- Connect to remote Linux servers
- Generate SSH keys
- Copy SSH keys to servers
- Configure SSH
- Transfer files securely
- Follow SSH security best practices

---

# 🤔 What is SSH?

SSH stands for **Secure Shell**.

It provides an encrypted connection between two computers.

Unlike Telnet, SSH encrypts all communication, making it secure against attackers.

---

# 📦 SSH Architecture

```text
+---------------------+
|     SSH Client      |
+----------+----------+
           |
     Encrypted Connection
           |
+----------+----------+
|     SSH Server      |
+---------------------+
```

---

# 🌐 Default SSH Port

SSH uses:

```text
22/TCP
```

Example:

```text
192.168.1.10:22
```

---

# 🔌 Connecting to a Server

Basic syntax:

```bash
ssh username@server_ip
```

Example:

```bash
ssh john@192.168.1.20
```

Using a domain:

```bash
ssh admin@example.com
```

---

# 🔑 SSH Key Authentication

Generate a new SSH key:

```bash
ssh-keygen
```

Recommended algorithm:

```bash
ssh-keygen -t ed25519
```

Generate RSA key:

```bash
ssh-keygen -t rsa -b 4096
```

---

# 📂 SSH Keys

Default location:

```text
~/.ssh/
```

Example:

```text
~/.ssh/

id_ed25519
id_ed25519.pub
known_hosts
config
```

| File | Purpose |
|------|---------|
| id_ed25519 | Private key |
| id_ed25519.pub | Public key |
| known_hosts | Known servers |
| config | SSH configuration |

---

# 📤 Copy Public Key

Copy your public key to a remote server.

```bash
ssh-copy-id user@server
```

Example:

```bash
ssh-copy-id john@192.168.1.20
```

---

# 🔐 Login Using SSH Key

```bash
ssh john@192.168.1.20
```

No password is required if key authentication is configured correctly.

---

# 📋 View Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Never share your **private key** (`id_ed25519`).

---

# ⚙ SSH Configuration

Edit the SSH config file:

```bash
nano ~/.ssh/config
```

Example:

```text
Host myserver
    HostName 192.168.1.20
    User john
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Now connect using:

```bash
ssh myserver
```

---

# 📁 Secure File Transfer

Copy a file to a server:

```bash
scp notes.txt john@192.168.1.20:/home/john
```

Download a file:

```bash
scp john@192.168.1.20:/home/john/report.txt .
```

Copy a directory:

```bash
scp -r Projects john@192.168.1.20:/home/john
```

---

# 🔄 Synchronize Files with rsync

```bash
rsync -av Projects/ john@192.168.1.20:/home/john/Projects
```

Useful for backups and deployments.

---

# 🔍 Check SSH Service

Ubuntu/Debian:

```bash
sudo systemctl status ssh
```

Start service:

```bash
sudo systemctl start ssh
```

Enable at boot:

```bash
sudo systemctl enable ssh
```

---

# 🔐 SSH Security Best Practices

✅ Use SSH keys instead of passwords.

✅ Disable root login.

✅ Use strong passphrases.

✅ Keep OpenSSH updated.

✅ Disable password authentication if possible.

✅ Use a firewall.

---

# ⚠ Common Mistakes

❌ Sharing your private key.

❌ Using weak passwords.

❌ Leaving SSH open to the internet without protection.

❌ Logging in as the root user directly.

---

# 🧪 Practice Lab

Complete these tasks:

1. Install OpenSSH Server.
2. Start the SSH service.
3. Generate an SSH key.
4. Copy the public key to a remote server.
5. Log in using the SSH key.
6. Transfer a file using `scp`.
7. Create a custom SSH configuration.

---

# 💻 Useful Commands

Generate key

```bash
ssh-keygen -t ed25519
```

Connect

```bash
ssh user@server
```

Copy key

```bash
ssh-copy-id user@server
```

Upload file

```bash
scp file.txt user@server:/home/user
```

Download file

```bash
scp user@server:/home/user/file.txt .
```

Check service

```bash
sudo systemctl status ssh
```

---

# ❓ Quiz

### 1. What does SSH stand for?

<details>
<summary>Answer</summary>

Secure Shell.

</details>

---

### 2. Which port does SSH use by default?

<details>
<summary>Answer</summary>

22/TCP

</details>

---

### 3. Which command generates a new SSH key?

<details>
<summary>Answer</summary>

```bash
ssh-keygen
```

</details>

---

### 4. Which file should never be shared?

<details>
<summary>Answer</summary>

Your private key (`id_ed25519` or `id_rsa`).

</details>

---

### 5. Which command copies your public key to a server?

<details>
<summary>Answer</summary>

```bash
ssh-copy-id user@server
```

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ What SSH is
- ✅ How to connect to remote servers
- ✅ SSH keys
- ✅ SSH configuration
- ✅ Secure file transfer
- ✅ SSH security best practices

---

# 🚀 Next Lesson

Continue to **Linux Processes**.

[:material-arrow-right: Linux Processes](processes.md){ .md-button .md-button--primary }
