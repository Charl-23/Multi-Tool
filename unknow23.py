import os
import sys
import time
import subprocess
from colorama import Fore, init

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

init(autoreset=True)

def slow_print(text, speed=0.05, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_bar():
    print(Fore.BLUE + "=" * 98)

def print_banner_ascii():
    banner_ascii = r"""
 ...    ::::::.    :::. :::  .   :::.    :::.    ...    .::    .   .:::        .:::.  .::.    
 ;;     ;;;`;;;;,  `;;; ;;; .;;,.`;;;;,  `;;; .;;;;;;;. ';;,  ;;  ;;;'        ,;'``;.;'`';;,  
[['     [[[  [[[[[. '[[ [[[[[/'    [[[[[. '[[,[[     \[[,'[[, [[, [['         ''  ,[['  .n[[  
$$      $$$  $$$ "Y$c$$_$$$$,      $$$ "Y$c$$$$$,     $$$  Y$c$$$c$P          .c$$P'   ``"$$$.
88    .d888  888    Y88"888"88o,   888    Y88"888,_ _,88P   "88"888          d88 _,oo, ,,o888"
 "YmmMMMM""  MMM     YM MMM "MMP"  MMM     YM  "YMMMMMP"     "M "M"          MMMUP*"^^ YMMP"  
                                                                                              
                                                                                              
                                                                                              
                     `::.  `::         `::                 `::.                               
                      ;;;   ;; ;;,      ;;                  ;;;                               
[ccc, ,cccc,  ,c  ,   [[[=[[[[[[.    =[[[[[[.,ccc,   ,ccc,  [[[                               
$$$$$$$$"$$$ $$'  $$$ $$'   $$ $$$ cccc $$  $$$"c$$$$$$"c$$$$$'                               
888 Y88" 888o888   888\8o   88,888      88, 888   88888   88\8o                               
MMM  M'  "MMM "YUM" MP MM;  MMMMMM      MMM  "YUMMP  "YUMMP  MM;    
 """
    print(Fore.GREEN + banner_ascii)

def run_tool(tool):
    try:
        subprocess.run(tool["cmd"], cwd=tool["path"])
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def print_tools_columns(tools, cols=3):
    keys = sorted(tools.keys(), key=lambda x: int(x))
    n = len(keys)
    rows = (n + cols - 1) // cols  

    matrix = []
    for r in range(rows):
        row_items = []
        for c in range(cols):
            idx = r + c * rows
            if idx < n:
                key = keys[idx]
                name = tools[key]['name']
                row_items.append(f"{key}. {name}")
            else:
                row_items.append("")  
        matrix.append(row_items)

    col_width = max(len(item) for row in matrix for item in row) + 4

    for row in matrix:
        line = ""
        for item in row:
            line += item.ljust(col_width)
        print(Fore.CYAN + line)

TOOLS = {
    "1": {"name": "Phishing", "path": os.path.join(BASE_DIR, "tools", "zphisher"), "cmd": ["sudo", "bash", "zphisher.sh"]},
    "2": {"name": "French-Osint", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "osint.py"]},
    "3": {"name": "Brute-Force-Insta", "path": os.path.join(BASE_DIR, "tools", "instainsane"), "cmd": ["sudo", "bash", "instainsane.sh"]},
    "4": {"name": "Change-IP", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["sudo", "bash", "ipghost.sh"]},
    "5": {"name": "DDoS", "path": os.path.join(BASE_DIR, "tools", "DDoS-Ripper"), "cmd": ["python3", "DRipper.py"]},
    "6": {"name": "Track-IP", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["bash", "trackip"]},
    "7": {"name": "Virus-Crafter", "path": os.path.join(BASE_DIR, "tools", "TigerVirus"), "cmd": ["bash", "TigerVirus.sh"]},
    "8": {"name": "WebSite-Scan", "path": os.path.join(BASE_DIR, "tools", "RED_HAWK"), "cmd": ["php", "rhawk.php"]},
    "9": {"name": "CamPhish", "path": os.path.join(BASE_DIR, "tools", "CamPhish"), "cmd": ["bash", "camphish.sh"]},
    "10": {"name": "HackerPro", "path": os.path.join(BASE_DIR, "tools", "hackerpro"), "cmd": ["python2", "hackerpro.py"]},
    "11": {"name": "Admin-hack", "path": os.path.join(BASE_DIR, "tools", "AdminHack"), "cmd": ["bash", "AdminHack.sh"]},
    "12": {"name": "report-tiktok", "path": os.path.join(BASE_DIR, "tools", "report-tiktok"), "cmd": ["python3", "main.py"]},
    "13": {"name": "Discord-spammer", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "Discord_MassDM.py"]},
    "14": {"name": "Mail-finder", "path": os.path.join(BASE_DIR, "tools", "MailFinder"), "cmd": ["Python3", "MailFinder.py"]},
    "15": {"name": "Admin-Finder", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "admin-panel-finder.py"]},
    "16": {"name": "publics-cameras", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "cam-hackers.py"]},
    "17": {"name": "Mail-sender", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "fakemail.py"]},
    "18": {"name": "google-dork", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "google-dorking.py"]},
    "19": {"name": "DDoS-2", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "hulk.py"]},
    "20": {"name": "mac-changer", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "mac-changer.py"]},
    "21": {"name": "DracNmap", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["bash", "dracnmap-v2.2.sh"]},
    "22": {"name": "steganography", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "steganography.py"]},
    "23": {"name": "free-views", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "video-views.py"]},
    "24": {"name": "Wifi-DoS", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "wifi_dos_final.py"]},
    "25": {"name": "Find-By-Username", "path": os.path.join(BASE_DIR, "tools", "sherlock"), "cmd": ["python3", "sherlock23.py"]},
    "26": {"name": "Instagrame-Report", "path": os.path.join(BASE_DIR, "tools", "Instagram-mass-report"), "cmd": ["python3", "InstaReporter.py"]},
    "27": {"name": "fsociety-logo", "path": os.path.join(BASE_DIR, "tools"), "cmd": ["python3", "fsociety-logo.py"]}
}

def main():
    clear_screen()
    print_bar()
    print_banner_ascii()
    print_bar()
    slow_print("[!] Only for educational purposes", 0.05, Fore.BLUE)
    slow_print("[!] I'm not responsible for your actions with this tool", 0.05, Fore.MAGENTA)
    print(Fore.CYAN + "GitHub: https://github.com/Charl-23\n")

    while True:
        print_tools_columns(TOOLS, cols=3)
        print(Fore.MAGENTA + "0. Quit\n")

        choice = input(Fore.GREEN + "Take your choice : ")
        if choice == "0":
            print(Fore.GREEN + "Bye and enjoy your hacking !")
            break  
        elif choice in TOOLS:
            run_tool(TOOLS[choice])
            input(Fore.YELLOW + "\nPress enter to go to the menu...")
            clear_screen()
            print_bar()
            print_banner_ascii()
            print_bar()
            slow_print("[!] Only for educational purposes", 0.01, Fore.BLUE)
            slow_print("[!] I'm not responsible for your actions with this tool", 0.01, Fore.MAGENTA)
            print(Fore.CYAN + "GitHub: https://github.com/Charl-23\n")
        else:
            print(Fore.RED + "Error: Invalid choice")

if __name__ == "__main__":
    main()
