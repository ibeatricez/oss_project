# 🛡️ Advanced Security Evasion Project – GitHub Tasks

This file contains structured tasks for your GitHub Project board. Each task is designed for one team member and can be copy-pasted into GitHub Issues.

---

## ✅ TASKS

---

### 👤 Person 1 – Attacker Techniques Specialist

---

#### 📌 [Person 1] Deploy and Test Keylogger

**Description:**  
Create or reuse a keylogger script. Execute it in a Windows environment and observe if Windows Defender or any EDR solution detects it.

**Checklist:**
- [ ] Find or write a keylogger script  
- [ ] Run it on test machine  
- [ ] Monitor antivirus/Defender logs  
- [ ] Record results and prepare short summary  

**Due Date:** 2025-04-10  
**Assigned To:** @person1-username

---

#### 📌 [Person 1] Hidden Commands & Process Hiding

**Description:**  
Run non-visible PowerShell commands and apply stealth techniques like process hollowing to hide execution. Track if they’re detected.

**Checklist:**
- [ ] Use PowerShell for hidden execution  
- [ ] Try process hollowing using tools (e.g., LOLBAS)  
- [ ] Check system logs for detection  
- [ ] Share findings with team  

**Due Date:** 2025-04-15  
**Assigned To:** @person1-username

---

### 👤 Person 2 – Security Monitoring & Defender Specialist

---

#### 📌 [Person 2] Configure Windows Defender & Logging Tools

**Description:**  
Set up Windows Defender with advanced settings. Enable logging tools such as Sysmon and Event Viewer for complete monitoring.

**Checklist:**
- [ ] Configure Defender rules and exclusions  
- [ ] Install and configure Sysmon  
- [ ] Enable relevant logging in Event Viewer  
- [ ] Capture initial system state  

**Due Date:** 2025-04-08  
**Assigned To:** @person2-username

---

#### 📌 [Person 2] Create Backdoor and Simulate Remote Access

**Description:**  
Create a backdoor using Metasploit or similar tools. Attempt a reverse shell connection and observe how Defender and logs respond.

**Checklist:**
- [ ] Generate backdoor payload  
- [ ] Establish remote access  
- [ ] Monitor Defender, Firewall, and Event Viewer  
- [ ] Document activity  

**Due Date:** 2025-04-12  
**Assigned To:** @person2-username

---

#### 📌 [Person 2] Collect and Share Logs with Team

**Description:**  
Export all relevant logs collected during attacks for analysis. Include Sysmon, Defender, and network data.

**Checklist:**
- [ ] Export Sysmon logs  
- [ ] Export Event Viewer logs  
- [ ] Annotate findings (e.g., timestamps, alerts)  
- [ ] Send to Person 3  

**Due Date:** 2025-04-16  
**Assigned To:** @person2-username

---

### 👤 Person 3 – Data Analyst & Reporting

---

#### 📌 [Person 3] Perform Process Injection & Memory Manipulation

**Description:**  
Use techniques like DLL injection and reflective DLL loading to test antivirus response. Analyze memory behavior.

**Checklist:**
- [ ] Perform DLL Injection  
- [ ] Try Reflective DLL loading  
- [ ] Track detection and system behavior  
- [ ] Log and prepare summary  

**Due Date:** 2025-04-13  
**Assigned To:** @person3-username

---

#### 📌 [Person 3] Implement and Test Persistence Techniques

**Description:**  
Apply persistence methods such as registry autoruns or scheduled tasks. Reboot the system and check if the payload stays active.

**Checklist:**
- [ ] Test registry autoruns  
- [ ] Create scheduled tasks  
- [ ] Reboot and verify persistence  
- [ ] Check for detection and record results  

**Due Date:** 2025-04-17  
**Assigned To:** @person3-username

---

#### 📌 [Person 3] Analyze Results & Prepare Final Report

**Description:**  
Aggregate all test results and generate a summary report comparing detection across techniques and solutions.

**Checklist:**
- [ ] Compare Defender vs. other tools  
- [ ] Build graphs/tables for detection success/failure  
- [ ] Write final report  
- [ ] Prepare slide deck (if needed)  

**Due Date:** 2025-04-20  
**Assigned To:** @person3-username