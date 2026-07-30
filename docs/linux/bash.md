# 📜 Bash Scripting

Bash (Bourne Again SHell) is the default command-line shell on most Linux distributions. It allows you to automate repetitive tasks by writing scripts.

---

## 🎯 Learning Objectives

After this lesson, you will be able to:

- Understand Bash scripting
- Create and execute Bash scripts
- Use variables
- Accept user input
- Work with conditions
- Use loops
- Create functions
- Automate basic Linux tasks

---

# 🤔 What is Bash?

Bash is a command-line interpreter that executes commands entered by the user or from a script file.

A Bash script is simply a text file containing Linux commands.

Example:

```bash
#!/bin/bash

echo "Hello World"
```

---

# 📝 Creating Your First Script

Create a new file:

```bash
touch hello.sh
```

Edit it:

```bash
nano hello.sh
```

Add:

```bash
#!/bin/bash

echo "Hello Cybersecurity!"
```

Save the file.

---

# 🔓 Make the Script Executable

```bash
chmod +x hello.sh
```

Run it:

```bash
./hello.sh
```

Output:

```text
Hello Cybersecurity!
```

---

# 🧾 Shebang

Every Bash script should begin with:

```bash
#!/bin/bash
```

This tells Linux to execute the file using the Bash interpreter.

---

# 📦 Variables

Create variables:

```bash
#!/bin/bash

name="Aditya"

echo $name
```

Output:

```text
Aditya
```

---

# ⌨️ User Input

```bash
#!/bin/bash

echo "Enter your name"

read name

echo "Hello $name"
```

---

# 🧮 Arithmetic Operations

```bash
#!/bin/bash

a=10
b=20

sum=$((a+b))

echo $sum
```

Output:

```text
30
```

---

# 🔀 If Statement

```bash
#!/bin/bash

age=20

if [ $age -ge 18 ]
then
    echo "Adult"
fi
```

---

# If-Else

```bash
#!/bin/bash

marks=40

if [ $marks -ge 35 ]
then
    echo "Pass"
else
    echo "Fail"
fi
```

---

# Multiple Conditions

```bash
#!/bin/bash

marks=85

if [ $marks -ge 90 ]
then
    echo "Grade A"
elif [ $marks -ge 75 ]
then
    echo "Grade B"
else
    echo "Grade C"
fi
```

---

# 🔁 For Loop

```bash
#!/bin/bash

for i in {1..5}
do
    echo $i
done
```

Output

```text
1
2
3
4
5
```

---

# 🔄 While Loop

```bash
#!/bin/bash

count=1

while [ $count -le 5 ]
do
    echo $count
    ((count++))
done
```

---

# 🔧 Functions

```bash
#!/bin/bash

hello(){

echo "Welcome!"

}

hello
```

---

# 📂 Working with Files

Check if a file exists.

```bash
#!/bin/bash

if [ -f notes.txt ]
then
    echo "File exists"
else
    echo "File not found"
fi
```

---

# 📁 Working with Directories

```bash
#!/bin/bash

if [ -d Projects ]
then
    echo "Directory exists"
fi
```

---

# 🖥 Useful System Variables

| Variable | Meaning |
|-----------|---------|
| `$USER` | Current user |
| `$HOME` | Home directory |
| `$PWD` | Current directory |
| `$HOSTNAME` | Computer name |
| `$PATH` | Executable search path |

Example:

```bash
echo $USER
```

---

# 📊 Exit Status

Every command returns an exit code.

```bash
echo $?
```

| Code | Meaning |
|------|---------|
| 0 | Success |
| Non-zero | Error |

---

# 🛡 Cybersecurity Automation Example

Create a simple backup script.

```bash
#!/bin/bash

mkdir Backup

cp *.txt Backup/

echo "Backup Completed"
```

---

# 🧪 Practice Lab

Create scripts that:

1. Print your name
2. Accept user input
3. Calculate two numbers
4. Display today's date
5. Check if a file exists
6. Print numbers from 1 to 10
7. Create a backup folder

---

# 💻 Practice Commands

Create script

```bash
touch script.sh
```

Edit

```bash
nano script.sh
```

Run

```bash
chmod +x script.sh

./script.sh
```

---

# ⚠ Common Mistakes

❌ Forgetting the shebang

❌ Forgetting execute permission

❌ Missing spaces inside `[ ]`

Wrong

```bash
if [$age -gt 18]
```

Correct

```bash
if [ $age -gt 18 ]
```

---

# ❓ Quiz

### 1. What does `#!/bin/bash` mean?

<details>
<summary>Answer</summary>

It tells Linux to execute the script using the Bash interpreter.

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

### 3. Which command runs a script?

<details>
<summary>Answer</summary>

```bash
./script.sh
```

</details>

---

### 4. Which variable stores the current user?

<details>
<summary>Answer</summary>

```text
$USER
```

</details>

---

### 5. What does exit code `0` mean?

<details>
<summary>Answer</summary>

The command executed successfully.

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ Bash basics
- ✅ Variables
- ✅ User input
- ✅ Conditions
- ✅ Loops
- ✅ Functions
- ✅ File handling
- ✅ Automation
- ✅ Exit codes

---

# 🚀 Next Lesson

Continue to **SSH (Secure Shell)**.

[:material-arrow-right: SSH](ssh.md){ .md-button .md-button--primary }
