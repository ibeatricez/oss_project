"""activity_logger.py
---------------------------------
Monitors CPU and RAM usage of a specific Windows process (by default the
Windows Defender engine) at fixed intervals and plots the results.

The script is meant to be executed on an **analysis / blue‑team VM** while
running stealth‑attack artefacts (key‑logger, reverse shell, etc.).
The plot helps correlate Defender resource spikes with the moments the attack
is active.

USAGE
-----
    python activity_logger.py                # 60 s, 2 s interval, default proc
    python activity_logger.py --duration 300 --interval 1 --process MsMpEng.exe

DEPENDENCIES
------------
    pip install psutil matplotlib

Author :  YOUR TEAM NAME
License:  MIT (for coursework purposes)
"""
import argparse
import time
from typing import List

import psutil
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
# 1. Command‑line arguments
# --------------------------------------------------------------------------- #
parser = argparse.ArgumentParser(
    description="""Sample CPU‑/memory‑usage of a single Windows process and
    visualise the result at the end of the run."""
)
parser.add_argument(
    "--process",
    default="MsMpEng.exe",   # Actual Defender engine on modern Windows
    help="Executable name of the process to monitor (case‑sensitive).")

parser.add_argument(
    "--duration", type=int, default=60,
    help="Total monitoring time in seconds.")

parser.add_argument(
    "--interval", type=float, default=2.0,
    help="Sampling interval in seconds (must be > 0.1 s).")

args = parser.parse_args()

PROCESS_NAME: str = args.process
MONITOR_DURATION: int = args.duration
SAMPLE_INTERVAL: float = max(0.1, args.interval)  # avoid overwhelming CPU

# --------------------------------------------------------------------------- #
# 2. Data containers
# --------------------------------------------------------------------------- #
timestamps: List[str] = []
cpu_usages: List[float] = []
memory_usages: List[float] = []

print(f"Monitoring {PROCESS_NAME} for {MONITOR_DURATION} s …")

start_time = time.time()

# --------------------------------------------------------------------------- #
# 3. Sampling loop
# --------------------------------------------------------------------------- #
while time.time() - start_time < MONITOR_DURATION:
    found = False

    # Enumerate all processes – asking only for the fields we need keeps the
    # syscall overhead minimal (< 1 ms on a modern CPU).
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        if proc.info["name"] == PROCESS_NAME:
            found = True

            # `cpu_percent(interval=0.1)` → 100 ms measurement window.
            cpu = proc.cpu_percent(interval=0.1)
            mem = proc.memory_percent()

            # Record human‑readable timestamp for the upcoming plot.
            timestamp = time.strftime("%H:%M:%S")
            timestamps.append(timestamp)
            cpu_usages.append(cpu)
            memory_usages.append(mem)

            print(f"[{timestamp}] CPU: {cpu:5.2f}%  |  MEM: {mem:5.2f}%")
            break

    if not found:
        # Process gone / not running – append placeholder zeros to keep arrays
        # aligned. Visual gap in the plot will highlight the disappearance.
        timestamp = time.strftime("%H:%M:%S")
        timestamps.append(timestamp)
        cpu_usages.append(0.0)
        memory_usages.append(0.0)
        print(f"[{timestamp}] {PROCESS_NAME} not found.")

    # Sleep until next sample.  We sleep *after* processing so that the very
    # first sample happens immediately.
    time.sleep(SAMPLE_INTERVAL)

# --------------------------------------------------------------------------- #
# 4. Plotting
# --------------------------------------------------------------------------- #
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(timestamps, cpu_usages, label="CPU Usage (%)")
plt.title(f"Resource usage of {PROCESS_NAME}")
plt.ylabel("CPU (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(timestamps, memory_usages, label="Memory Usage (%)")
plt.xlabel("Time (HH:MM:SS)")
plt.ylabel("Memory (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
