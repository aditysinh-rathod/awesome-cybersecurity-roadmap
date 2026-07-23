# 🐚 Bash Scripting

## 📖 Overview

Bash (Bourne Again Shell) is the default command-line interpreter for most Linux distributions. It allows users to automate repetitive tasks, manage systems, and build powerful command-line tools.

---

# 🎯 Why Learn Bash?

- Automate repetitive tasks
- Manage servers efficiently
- Write custom security tools
- Parse logs
- Schedule jobs
- Save time

---

# 📝 Your First Script

```bash
#!/bin/bash

echo "Hello, Cybersecurity!"
```

Run:

```bash
chmod +x hello.sh
./hello.sh
```

---

# 📦 Variables

```bash
name="Aditysinh"

echo $name
```

---

# 📥 User Input

```bash
read -p "Enter your name: " user

echo "Welcome $user"
```

---

# 🔀 Conditions

```bash
if [ -f test.txt ]
then
    echo "File exists"
else
    echo "File not found"
fi
```

---

# 🔁 Loops

```bash
for i in {1..5}
do
    echo $i
done
```

---

# ⚙️ Functions

```bash
greet(){

echo "Welcome!"

}

greet
```

---

# 🛡 Cybersecurity Use Cases

- Backup automation
- Log analysis
- User auditing
- Port checking
- System monitoring
- Malware scanning automation

---

# 📚 Practice

- Create a backup script
- Build a system information script
- Automate user creation
