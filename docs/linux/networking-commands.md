# 🌐 Linux Networking Commands

Networking is one of the most important skills in Linux and cybersecurity. Linux provides powerful command-line tools to inspect, troubleshoot, and analyze networks.

---

# 🎯 Learning Objectives

After completing this lesson, you will be able to:

- View network interfaces
- Check IP addresses
- Test connectivity
- Troubleshoot DNS
- Inspect open ports
- Capture network traffic
- Download files from the internet
- Diagnose network problems

---

# 🌍 Check IP Address

Show all network interfaces

```bash
ip addr
```

or

```bash
ip a
```

Example Output

```text
2: eth0
    inet 192.168.1.100/24
```

---

# 📡 Show Network Interfaces

```bash
ip link
```

Older systems

```bash
ifconfig
```

---

# 🌐 Check Routing Table

```bash
ip route
```

or

```bash
route -n
```

---

# 📍 Display Hostname

```bash
hostname
```

Display IP

```bash
hostname -I
```

---

# 🛰 Test Connectivity

Ping Google

```bash
ping google.com
```

Ping specific number

```bash
ping -c 4 google.com
```

---

# 🛣 Trace Network Path

```bash
traceroute google.com
```

Ubuntu Installation

```bash
sudo apt install traceroute
```

---

# 🔍 DNS Lookup

Using nslookup

```bash
nslookup google.com
```

Using dig

```bash
dig google.com
```

Reverse lookup

```bash
dig -x 8.8.8.8
```

---

# 🌍 Download Web Pages

Using curl

```bash
curl https://example.com
```

Show headers

```bash
curl -I https://example.com
```

Download file

```bash
curl -O https://example.com/file.zip
```

---

# 📥 Download Files

Using wget

```bash
wget https://example.com/file.zip
```

Resume download

```bash
wget -c https://example.com/file.zip
```

---

# 🔌 View Listening Ports

Modern command

```bash
ss -tuln
```

Older command

```bash
netstat -tuln
```

---

# 👀 View Active Connections

```bash
ss -tunap
```

---

# 🔍 Find Process Using Port

Example

```bash
sudo lsof -i :80
```

Port 22

```bash
sudo lsof -i :22
```

---

# 📊 Monitor Bandwidth

Install

```bash
sudo apt install iftop
```

Run

```bash
sudo iftop
```

---

# 📦 Capture Network Traffic

Using tcpdump

Capture packets

```bash
sudo tcpdump
```

Capture interface

```bash
sudo tcpdump -i eth0
```

Save capture

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

---

# 🦈 Analyze Packets

Open capture

```bash
wireshark capture.pcap
```

---

# 🔥 Check Open Ports

```bash
sudo nmap localhost
```

Specific host

```bash
sudo nmap 192.168.1.100
```

Install Nmap

```bash
sudo apt install nmap
```

---

# 🔐 Check SSH Connection

```bash
ssh user@192.168.1.20
```

Verbose output

```bash
ssh -v user@192.168.1.20
```

---

# 📂 Transfer Files

Upload

```bash
scp report.txt user@server:/home/user
```

Download

```bash
scp user@server:/home/user/report.txt .
```

---

# 🌍 Display Network Configuration

```bash
nmcli device show
```

---

# 📈 Network Diagnostics

Display socket statistics

```bash
ss -s
```

Network statistics

```bash
netstat -s
```

---

# 🛡 Cybersecurity Use Cases

These commands are commonly used for:

- Network troubleshooting
- Incident response
- Penetration testing
- Threat hunting
- Malware analysis
- Server administration

---

# ⚠ Common Mistakes

❌ Running packet capture without root privileges.

❌ Forgetting firewall rules.

❌ Using `ping` as the only troubleshooting tool.

❌ Ignoring DNS issues.

---

# 🧪 Practice Lab

Complete these tasks.

1. Find your IP address.
2. Ping Google.
3. Display your routing table.
4. Perform a DNS lookup.
5. Capture 20 packets using tcpdump.
6. Scan localhost with Nmap.
7. View open ports.
8. Download a file using wget.

---

# 💻 Practice Commands

Show IP

```bash
ip a
```

Ping

```bash
ping -c 4 google.com
```

DNS

```bash
dig openai.com
```

Open ports

```bash
ss -tuln
```

Capture

```bash
sudo tcpdump
```

Scan

```bash
sudo nmap localhost
```

Download

```bash
wget https://example.com/file.zip
```

---

# ❓ Quiz

### 1. Which command displays your IP address?

<details>
<summary>Answer</summary>

```bash
ip addr
```

</details>

---

### 2. Which command tests connectivity?

<details>
<summary>Answer</summary>

```bash
ping
```

</details>

---

### 3. Which command performs a DNS lookup?

<details>
<summary>Answer</summary>

```bash
dig
```

or

```bash
nslookup
```

</details>

---

### 4. Which command captures network packets?

<details>
<summary>Answer</summary>

```bash
tcpdump
```

</details>

---

### 5. Which tool scans open ports?

<details>
<summary>Answer</summary>

```bash
nmap
```

</details>

---

# 📚 Summary

In this lesson you learned:

- ✅ IP configuration
- ✅ Network interfaces
- ✅ Routing
- ✅ DNS tools
- ✅ Connectivity testing
- ✅ Port inspection
- ✅ Packet capture
- ✅ Network diagnostics
- ✅ Secure file transfer

---

# 🎉 Linux Module Completed!

Congratulations! You have completed the Linux module.

You now understand:

- ✅ Linux Basics
- ✅ File System
- ✅ Permissions
- ✅ Bash Scripting
- ✅ SSH
- ✅ Processes
- ✅ Package Management
- ✅ Networking Commands

---

# 🚀 Next Module

Continue your journey with **Networking Fundamentals**.

[:material-arrow-right: Start Networking Module](../networking/index.md){ .md-button .md-button--primary }
