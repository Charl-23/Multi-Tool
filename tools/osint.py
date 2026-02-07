import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, speed=0.03, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

os.system("clear")


os.system("figlet -c -f mono12 UNKNOW 23 ")
print(Fore.BLUE + "="*176)
slow_print("[+] Initializing modules...")
time.sleep(0.5)
slow_print("[+] Access granted to the dark web...")
time.sleep(0.5)
slow_print("[+] Loading Chromium engine...")
time.sleep(0.5)
slow_print("[+] Preparing application mode...")
time.sleep(0.5)
print(Fore.BLUE + "="*176)


for i in range(0, 101, 10):
    sys.stdout.write(Fore.CYAN + f"\r[+] Progress: {i}%")
    sys.stdout.flush()
    time.sleep(0.2)

print("\n" + Fore.GREEN + "[✓] Launching Osint application...")


url = "https://breach2bz.com"
os.system(f"chromium --app={url} >/dev/null 2>&1 &")

slow_print("[✓] Done. Enjoy you hacking by UNKNOW23.", 0.05, Fore.BLUE)
