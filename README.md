# oss_project

## Explore the Security of Windows with Hidden Commands
This project involves inspecting the vulnerabilities of the Windows OS by embedding hidden commands within images or audio files. The goal is to establish a TCP/UDP channel between Kali Linux(acting as the attacker)  and Windows. By default, Windows does not accept undefined TCP/UDP connections, which makes the project both intriguing and educational.
### Steps:
• Generate and embed a hidden command within a file.
• Download and execute the file on a Windows(VM)
• Inspect Windows' defending system during the download and running potential threat.
• Identify methods to make the threat detectable if it currently evades detection.
### Objectives:
• Create hidden commands within files.
• Establish a communication channel between two operating systems.
• Learn about defending systems, antiviruses, malware, and system tracking tools.
### References:
• Kali Linux, Stegosuite, Steghide, Netcat
• Windows 11 Defender
