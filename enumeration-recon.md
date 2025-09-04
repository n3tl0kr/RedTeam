# 🔍 Reconnaissance Cheatsheet

> **Practical Network Discovery, Service Enumeration, and Intelligence Gathering** - Quick reference for active and passive reconnaissance operations.

---

## 🎯 Quick Start Commands

### **Basic Network Discovery**
```bash
# Quick network scan
nmap -sn 192.168.1.0/24

# Fast port scan
nmap -F 192.168.1.1

# Service version detection
nmap -sV -sC 192.168.1.1

# Aggressive scan (be careful!)
nmap -A -T4 192.168.1.1
```

### **Subdomain Enumeration**
```bash
# Using subfinder
subfinder -d example.com -o subdomains.txt

# Using amass
amass enum -d example.com

# Using gobuster
gobuster dns -d example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt

# Using assetfinder
assetfinder example.com > subdomains.txt
```

---

## 🌐 Passive Reconnaissance (OSINT)

### **Domain Intelligence**
```bash
# WHOIS lookup
whois example.com

# DNS enumeration
dig example.com ANY
dig example.com MX
dig example.com NS

# Reverse DNS lookup
dig -x 8.8.8.8

# DNS zone transfer (if allowed)
dig @ns1.example.com example.com AXFR
```

### **Email & Social Media**
```bash
# Email format discovery
theHarvester -d example.com -b google

# Social media search
# Use tools like: sherlock, maigret, social-analyzer
sherlock username
maigret username
social-analyzer --username username --websites
```

### **Company Research**
```bash
# Company information
# Use: LinkedIn, Crunchbase, OpenCorporates
# Check SEC filings, company registries
# Research funding, acquisitions, partnerships
```

---

## 🚀 Active Reconnaissance

### **Network Scanning**

#### **Nmap Commands**
```bash
# Host discovery
nmap -sn 192.168.1.0/24                    # Ping scan
nmap -PS 192.168.1.0/24                    # TCP SYN ping
nmap -PA 192.168.1.0/24                    # TCP ACK ping
nmap -PU 192.168.1.0/24                    # UDP ping

# Port scanning
nmap -p 80,443,8080 192.168.1.1           # Specific ports
nmap -p- 192.168.1.1                      # All ports
nmap -p 1-1000 192.168.1.1                # Port range

# Service detection
nmap -sV 192.168.1.1                      # Version detection
nmap -sC 192.168.1.1                      # Default scripts
nmap --script=vuln 192.168.1.1            # Vulnerability scripts
```

#### **Masscan (Fast Scanning)**
```bash
# Fast port scan
masscan 192.168.1.0/24 -p 80,443,8080

# Full port scan
masscan 192.168.1.0/24 -p 0-65535

# Rate limiting
masscan 192.168.1.0/24 -p 80 --rate 1000
```

### **Service Enumeration**

#### **Web Services**
```bash
# Directory enumeration
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt
dirb http://example.com
dirsearch -u http://example.com

# Virtual host discovery
gobuster vhost -u http://example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt

# Technology detection
whatweb example.com
wappalyzer example.com
```

#### **SMB Enumeration**
```bash
# SMB enumeration
enum4linux 192.168.1.1
smbmap -H 192.168.1.1
smbclient -L //192.168.1.1

# SMB user enumeration
rpcclient -U "" -N 192.168.1.1
enum4linux -U 192.168.1.1
```

#### **SNMP Enumeration**
```bash
# SNMP walk
snmpwalk -v1 -c public 192.168.1.1
snmpwalk -v2c -c public 192.168.1.1

# SNMP enumeration
onesixtyone -c /usr/share/wordlists/SecLists/Discovery/SNMP/common-snmp-community-strings.txt 192.168.1.1
```

### **Web Application Enumeration**

#### **Common Vulnerabilities**
```bash
# SQL injection testing
sqlmap -u "http://example.com/page?id=1"

# XSS testing
# Use: Burp Suite, OWASP ZAP, custom scripts

# File inclusion
# Test: ?file=../../../etc/passwd
# Test: ?page=../../../../etc/passwd
```

#### **API Discovery**
```bash
# Common API endpoints
curl -X GET http://example.com/api/
curl -X GET http://example.com/api/v1/
curl -X GET http://example.com/rest/

# API documentation
# Check: /api/docs, /swagger, /openapi.json
```

---

## 🔍 Advanced Techniques

### **Cloud Infrastructure**

#### **AWS Reconnaissance**
```bash
# AWS CLI enumeration
aws sts get-caller-identity
aws iam list-users
aws s3 ls
aws ec2 describe-instances

# S3 bucket discovery
aws s3 ls s3://bucket-name/
aws s3 cp s3://bucket-name/file.txt ./
```

#### **Azure Reconnaissance**
```bash
# Azure CLI enumeration
az account show
az vm list
az storage account list
az webapp list
```

### **Container & Kubernetes**
```bash
# Docker enumeration
docker ps
docker images
docker exec -it container_id /bin/bash

# Kubernetes enumeration
kubectl get pods
kubectl get services
kubectl get secrets
kubectl get configmaps
```

### **IoT & Embedded Systems**
```bash
# Device discovery
nmap -sU -p 161 192.168.1.0/24              # SNMP devices
nmap -p 1883 192.168.1.0/24                 # MQTT devices
nmap -p 5683 192.168.1.0/24                 # CoAP devices

# Firmware analysis
# Use: binwalk, firmware-mod-kit, ghidra
binwalk firmware.bin
```

---

## 🛠️ Custom Scripts & Automation

### **Bash Recon Scripts**

#### **Quick Network Recon**
```bash
#!/bin/bash
# quick_recon.sh

TARGET=$1
echo "Starting reconnaissance on $TARGET"

# Host discovery
echo "=== Host Discovery ==="
nmap -sn $TARGET/24

# Port scan
echo "=== Port Scan ==="
nmap -sV -sC $TARGET

# Web enumeration
echo "=== Web Enumeration ==="
if curl -s http://$TARGET > /dev/null; then
    whatweb $TARGET
    gobuster dir -u http://$TARGET -w /usr/share/wordlists/dirb/common.txt -q
fi
```

#### **Subdomain Enumeration**
```bash
#!/bin/bash
# subdomain_enum.sh

DOMAIN=$1
echo "Enumerating subdomains for $DOMAIN"

# Create output directory
mkdir -p $DOMAIN

# Multiple tools
echo "Using subfinder..."
subfinder -d $DOMAIN -o $DOMAIN/subfinder.txt

echo "Using amass..."
amass enum -d $DOMAIN -o $DOMAIN/amass.txt

echo "Using assetfinder..."
assetfinder $DOMAIN > $DOMAIN/assetfinder.txt

# Combine and sort
cat $DOMAIN/*.txt | sort -u > $DOMAIN/all_subdomains.txt
echo "Found $(wc -l < $DOMAIN/all_subdomains.txt) unique subdomains"
```

### **Python Recon Scripts**

#### **Port Scanner**
```python
#!/usr/bin/env python3
import socket
import threading
import time

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass

def port_scanner(target, start_port=1, end_port=1024):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        time.sleep(0.01)  # Rate limiting

if __name__ == "__main__":
    target = input("Enter target IP: ")
    port_scanner(target)
```

#### **Subdomain Brute Forcer**
```python
#!/usr/bin/env python3
import requests
import dns.resolver
import sys

def check_subdomain(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    
    try:
        # DNS resolution
        dns.resolver.resolve(full_domain, 'A')
        print(f"[+] Found: {full_domain}")
        return True
    except:
        return False

def subdomain_brute(domain, wordlist_file):
    with open(wordlist_file, 'r') as f:
        subdomains = [line.strip() for line in f]
    
    print(f"Checking {len(subdomains)} subdomains...")
    
    for subdomain in subdomains:
        check_subdomain(domain, subdomain)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 subdomain_brute.py <domain> <wordlist>")
        sys.exit(1)
    
    domain = sys.argv[1]
    wordlist = sys.argv[2]
    subdomain_brute(domain, wordlist)
```

---

## 📊 Output & Documentation

### **Report Templates**

#### **Basic Recon Report**
```markdown
# Reconnaissance Report - [TARGET]

## Executive Summary
Brief overview of findings

## Scope
- Target: [IP/DOMAIN]
- Date: [DATE]
- Tools Used: [LIST]

## Findings

### Network Discovery
- Live hosts: [LIST]
- Open ports: [DETAILS]

### Service Enumeration
- Web services: [DETAILS]
- Database services: [DETAILS]
- File services: [DETAILS]

### Vulnerabilities
- [LIST AND SEVERITY]

## Recommendations
- [ACTION ITEMS]

## Appendices
- [SCAN OUTPUTS]
- [SCREENSHOTS]
```

### **Data Organization**
```bash
# Create organized directory structure
mkdir -p recon/{nmap,web,services,outputs}
mkdir -p recon/web/{dirs,subdomains,technologies}
mkdir -p recon/services/{smb,ftp,ssh,http}
```

---

## 🚨 Legal & Ethical Considerations

### **Authorization Checklist**
- [ ] Written permission obtained
- [ ] Scope clearly defined
- [ ] Time constraints established
- [ ] Contact information exchanged
- [ ] Legal requirements reviewed

### **Responsible Disclosure**
```bash
# Document everything
# Respect rate limits
# Don't cause disruption
# Report findings responsibly
```

---

## 🔮 Advanced Reconnaissance

### **Social Engineering Recon**
```bash
# LinkedIn research
# Company employee information
# Technology stack discovery
# Organizational structure mapping
```

### **Physical Reconnaissance**
```bash
# Site surveys
# Dumpster diving (if authorized)
# Social engineering
# Physical access testing
```

### **Wireless Reconnaissance**
```bash
# WiFi scanning
airmon-ng start wlan0
airodump-ng wlan0mon

# Bluetooth enumeration
hcitool scan
bluetoothctl scan on
```

---

## 📚 Quick Reference

### **Common Ports**
```bash
# Web
80, 443, 8080, 8443

# Database
21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995

# File Services
21, 22, 139, 445

# Remote Access
22, 23, 3389, 5900
```

### **Useful Wordlists**
```bash
# Common wordlists
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
/usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
/usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt
```

### **Essential Tools**
```bash
# Network
nmap, masscan, netcat, wireshark

# Web
gobuster, dirb, nikto, whatweb

# OSINT
theHarvester, subfinder, amass, maltego

# Custom
custom scripts, automation frameworks
```

---

## 🤝 Contributing

We welcome contributions to expand this reconnaissance cheatsheet! Please:

- **Add new commands** and techniques
- **Share custom scripts** and automation
- **Update tool information** and examples
- **Contribute learning resources**
- **Report broken links** or outdated information

---

## 📞 Get Involved

- **GitHub Discussions**: [RedTeam Discussions](https://github.com/n3tl0kr/RedTeam/discussions)
- **Security Community**: Join reconnaissance and OSINT groups
- **Bug Bounty Programs**: Practice on authorized platforms
- **CTF Competitions**: Participate in capture the flag events

---

<div align="center">
  <sub>🔍 *"Reconnaissance is the foundation of every successful operation"* 🔍</sub>
</div>
