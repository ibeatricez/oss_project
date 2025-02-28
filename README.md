# oss_project

## Advanced Security Evasion in Windows with Hidden Commands

### Project Objective: 
Evaluate how well different security solutions can detect and respond to stealthy attack techniques, including hidden command execution, keyloggers, process injection, backdoors, and persistence mechanisms. The objective is to evaluate the detection capabilities of Windows Defender and third-party antivirus/EDR solutions by logging system behavior, network activity, and event logs.
### Project Expectations: 
This project involves inspecting the vulnerabilities of the Windows OS by embedding hidden commands within images or audio files. The goal is to establish a TCP/UDP channel between Kali Linux(acting as the attacker)  and Windows. By default, Windows does not accept undefined TCP/UDP connections, which makes the project both intriguing and educational.
### Steps for Hidden Command within a file:
- Generate and embed a hidden command within a file.
- Download and execute the file on a Windows(VM)
- Inspect Windows' defending system during the download and running potential threat.
- Identify methods to make the threat detectable if it currently evades detection.
### Objectives for Hidden Command within a file:
- Create hidden commands within files.
- Establish a communication channel between two operating systems.
- Learn about defending systems, antiviruses, malware, and system tracking tools.
### References:
1. *Non-Visual Command Execution & Process Hiding** 
   - LOlbins Project. (2024). *Living Off The Land Binaries and Scripts (LOLBAS).* Retrieved from https://lolbas-project.github.io/
   - Microsoft Docs. (2023). *Using PowerShell for Automation and Hidden Execution.* Retrieved from https://learn.microsoft.com/en-us/powershell/ 

2. *Keylogger Deployment & Detection*
   - Malwarebytes Labs. (2023). *How Keyloggers Work and How to Prevent Them.* Retrieved from https://www.malwarebytes.com/keyloggers
   - Microsoft Defender Research Team. (2023). *Detecting Keystroke Logging with Windows Security Solutions.* Retrieved from https://www.microsoft.com/security/blog

3. *Backdoor Creation & Remote Access*
   - Offensive Security. (2024). *Metasploit Framework: Implementing Persistent Backdoors.* Retrieved from https://www.offensive-security.com/metasploit-unleashed/persistent-backdoors
   - Rapid7. (2023). *Using Netcat for Backdoor and Reverse Shell Access.* Retrieved from https://docs.rapid7.com/metasploit

4. *Process Injection & Memory Manipulation*
   - Mandiant Threat Intelligence. (2023). *Understanding Process Hollowing and Memory Injection.* Retrieved from https://www.mandiant.com/resources/process-hollowing 
   - Red Team Journal. (2024). *Reflective DLL Injection Techniques for Penetration Testers.* Retrieved from https://www.redteamjournal.com/dll-injection

5. *Persistence Techniques & Detection* 
   - MITRE ATT&CK Framework. (2024). *Persistence Techniques Used by Malware.* Retrieved from https://attack.mitre.org/techniques/T1053/
   - Sysinternals. (2023). *Using Autoruns for Windows to Identify Malware Persistence.* Retrieved from https://docs.microsoft.com/en-us/sysinternals/

6. *Windows Security Tests & Log Analysis*  
   - Microsoft. (2023). *Windows Defender Antivirus Testing Guide.* Retrieved from https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/ 
   - Elastic Security. (2024). *Using ELK Stack for Security Monitoring & Log Analysis.* Retrieved from https://www.elastic.co/security
