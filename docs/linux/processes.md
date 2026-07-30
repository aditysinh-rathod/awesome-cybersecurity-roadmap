# ⚙️ Linux Processes

Every program running on Linux is called a **process**. Understanding processes is essential for system administration, troubleshooting, performance tuning, and cybersecurity.

---

# 🎯 Learning Objectives

After completing this lesson, you will be able to:

- Understand what a process is
- Identify process states
- View running processes
- Monitor system performance
- Kill and manage processes
- Understand foreground and background jobs
- Set process priorities

---

# 🤔 What is a Process?

A **process** is an instance of a running program.

For example:

- Google Chrome
- VS Code
- Python Script
- SSH Server

Each running program gets its own **Process ID (PID)**.

---

# 🏗 Process Lifecycle

```text
New
 │
 ▼
Ready
 │
 ▼
Running
 │
 ├─────────────► Waiting
 │                 │
 ▼                 │
Terminated ◄───────┘
```

---

# 📊 Process States

| State | Meaning |
|--------|---------|
| R | Running |
| S | Sleeping |
| D | Waiting for I/O |
| T | Stopped |
| Z | Zombie |

---

# 🔍 View Running Processes

Show current shell processes

```bash
ps
```

Show all processes

```bash
ps -e
```

Detailed view

```bash
ps -ef
```

User-oriented format

```bash
ps aux
```

---

# 📈 Monitor Processes

Launch the interactive monitor

```bash
top
```

If installed

```bash
htop
```

`htop` provides a more user-friendly interface.

---

# 🔎 Search for a Process

Find a process by name

```bash
ps aux | grep firefox
```

Or

```bash
pgrep firefox
```

---

# 🛑 Kill a Process

Kill by PID

```bash
kill 1234
```

Force kill

```bash
kill -9 1234
```

Kill by name

```bash
pkill firefox
```

---

# 🚦 Foreground & Background

Run normally

```bash
python app.py
```

Run in background

```bash
python app.py &
```

View background jobs

```bash
jobs
```

Bring a job to foreground

```bash
fg
```

Move a job to background

```bash
bg
```

---

# 🧠 Process Priority

Lower priority

```bash
nice -n 10 python script.py
```

View priorities

```bash
top
```

Change priority

```bash
renice 5 -p 1234
```

---

# 👨‍👩‍👧 Parent & Child Processes

Every process has:

- Parent Process (PPID)
- Child Process

View process tree

```bash
pstree
```

---

# 🧾 Process Information

Find PID

```bash
pidof sshd
```

View details

```bash
ps -p 1234 -f
```

---

# ⏱ Real-Time Monitoring

Monitor CPU usage

```bash
top
```

Monitor memory

```bash
free -h
```

Monitor disk usage

```bash
df -h
```

Monitor I/O

```bash
iostat
```

---

# 🔐 Security Tips

✅ Kill suspicious processes.

✅ Investigate unknown high CPU usage.

✅ Monitor long-running background jobs.

✅ Review process ownership.

---

# ⚠ Common Mistakes

❌ Killing system processes.

❌ Using `kill -9` without checking first.

❌ Running unnecessary background services.

---

# 🧪 Practice Lab

Complete these tasks:

1. Open a new terminal.
2. Start the `sleep` command.
3. Find its PID.
4. Kill the process.
5. Launch a process in the background.
6. View all background jobs.
7. Display the process tree.

---

# 💻 Practice Commands

Start a process

```bash
sleep 300
```

Find PID

```bash
ps aux | grep sleep
```

Kill it

```bash
kill PID
```

Run in background

```bash
sleep 600 &
```

List jobs

```bash
jobs
```

Show process tree

```bash
pstree
```

---

# ❓ Quiz

### 1. What is a PID?

<details>
<summary>Answer</summary>

Process ID.

</details>

---

### 2. Which command shows all running processes?

<details>
<summary>Answer</summary>

```bash
ps -ef
```

</details>

---

### 3. Which command launches the interactive process monitor?

<details>
<summary>Answer</summary>

```bash
top
```

</details>

---

### 4. Which command forcefully kills a process?

<details>
<summary>Answer</summary>

```bash
kill -9 PID
```

</details>

---

### 5. Which command lists background jobs?

<details>
<summary>Answer</summary>

```bash
jobs
```

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ What a process is
- ✅ Process states
- ✅ Viewing processes
- ✅ Monitoring CPU and memory
- ✅ Killing processes
- ✅ Background jobs
- ✅ Process priorities
- ✅ Parent and child processes

---

# 🚀 Next Lesson

Continue to **Package Management**.

[:material-arrow-right: Package Management](package-management.md){ .md-button .md-button--primary }
