import psutil
import time
import matplotlib.pyplot as plt

# Process name for Windows Defender
defender_process_name = "SecurityHealthService.exe"

# Data storage
timestamps = []
cpu_usages = []
memory_usages = []

# Duration to monitor (in seconds)a
monitor_duration = 60
interval = 2  # seconds between samples

start_time = time.time()

print("Monitoring Windows Defender (MsMpEng.exe)...")

while time.time() - start_time < monitor_duration:
    found = False
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        if proc.info['name'] == defender_process_name:
            found = True
            cpu = proc.cpu_percent(interval=0.1)  # get CPU usage (non-blocking)
            mem = proc.memory_percent()
            timestamp = time.strftime('%H:%M:%S')
            timestamps.append(timestamp)
            cpu_usages.append(cpu)
            memory_usages.append(mem)
            print(f"[{timestamp}] CPU: {cpu:.2f}%, Memory: {mem:.2f}%")
            break
    if not found:
        print("Defender process not found.")
    time.sleep(interval)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(timestamps, cpu_usages, label='CPU Usage (%)', color='red')
plt.title('Windows Defender Resource Usage')
plt.ylabel('CPU (%)')
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(timestamps, memory_usages, label='Memory Usage (%)', color='blue')
plt.xlabel('Time')
plt.ylabel('Memory (%)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
