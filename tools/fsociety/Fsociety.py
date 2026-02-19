#!/usr/bin/env python3
import os, sys, time

# ========= UTILS =========
def clear():
    os.system("clear")

def slowprint(s, speed=0.02):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)

# ========= BANNER =========
clear()
print("""\033[92m
=========================================================================
|       __________                  _____     _____                     |
|       ___  ____/_____________________(_)______  /_____  __            |
|       __  /_   __  ___/  __ \\  ___/_  /_  _ \\  __/_  / / /            |
|       _  __/   _(__  )/ /_/ / /__ _  / /  __/ /_ _  /_/ /             |
|       /_/      /____/ \\____/\\___/ /_/  \\___/\\__/ _\\__, /              |
|                                                      /____/           |
|      A Offensive Python Script - Inspired by Mr.Robot                 |
|      Github : https://github.com/Charl-23                             |
=========================================================================
""")

slowprint("\033[91m[*] F**K SOCIETY : Penetration Testing Toolkit", 0.01)
input("\n\033[97m[*] Press Enter To Boot ")
clear()

slowprint("[*] Booting.....", 0.02)
time.sleep(0.5)
slowprint("\033[97m[*] Booting Completed ✓")
time.sleep(1)
clear()

# ========= MENU =========
TOOLS = [
    ("01", "Check Anonymity", "python tools/amianonymous.py"),
    ("02", "Admin Panel Finder", "python tools/admin-panel-finder.py"),
    ("03", "ARP Spoofing", "sudo python tools/arp-spoofing.py"),
    ("04", "Banner Grabbing", "python tools/banner-grabbing.py"),
    ("05", "HULK DDOS", "python tools/hulk.py"),
    ("06", "Fake Mail", "python tools/fakemail.py"),
    ("07", "Fake Credentials", "python tools/fake-data-generator.py"),
    ("08", "Gmail Hacking", "python tools/hack-gmail.py"),
    ("09", "IP Scanner", "python tools/ip-scanner.py"),
    ("10", "Linux Password Cracker", "python tools/linux_pass_cracker.py"),
    ("11", "Password Generator", "python tools/pass-gen.py"),
    ("12", "Nmap Scanner", "python tools/nmap_port_scanner.py"),
    ("13", "WiFi DDOS", "python tools/wifi_dos_final.py"),
    ("14", "PDF Exif Tool", "python tools/pdf-exif-tool.py"),
    ("15", "Steganography", "python tools/steganography.py"),
    ("16", "Get WiFi Password", "python tools/get_wifipass.py"),
    ("17", "Internet Speed Test", "python tools/internet-speed-test.py"),
    ("18", "Network Monitoring", "python tools/network-monitoring.py"),
    ("19", "Movie Suggestion", "python tools/movie-suggesting.py"),
    ("20", "Anonsurf Start", "anonsurf start"),
    ("21", "Anonsurf Stop", "anonsurf stop"),
    ("22", "Python Emulator", "python tools/terminal-emulator.py"),
    ("23", "Calculator", "python tools/calculator.py"),
    ("24", "ARP Checking", "arp -a"),
    ("25", "SMS Spoofing", "python tools/fakesms.py"),
    ("26", "Nano Editor", "nano"),
    ("27", "Phishing Attack", "python tools/pyphisher.py"),
    ("28", "SMS Bombing", "python tools/bomber.py"),
    ("29", "Phone Number OSINT", "python tools/phone-number-info.py"),
    ("30", "XSS Finder", "python tools/xss-vulnerability-finder.py"),
    ("31", "SQLi Finder", "python tools/sqli-scanner.py"),
    ("32", "Shodan", "python tools/shodan-api.py"),
    ("33", "System Info", "python tools/sys-info.py"),
    ("34", "Netdiscover", "netdiscover"),
    ("35", "MAC Changer", "python tools/mac-changer.py"),
    ("36", "Encrypt/Decrypt GUI", "python tools/none-read-my-code.py"),
    ("37", "Encrypt Message", "python tools/encrypt.py"),
    ("38", "Decrypt Message", "python tools/decrypt.py"),
    ("39", "Translator", "python tools/translator.py"),
    ("40", "Terminal Emulator", "python tools/terminal-emulator.py"),
    ("41", "OSINT", "python tools/osint.py"),
    ("42", "HULK Browser GUI", "python hulk-browser.py"),
    ("43", "Email Bombing", "python tools/email-bomber.py"),
    ("44", "Social Media Automation", "python tools/automate-social_media-video-views.py"),
    ("45", "Hulk Search Engine", "python tools/hulk-engine.py"),
    ("46", "Google Dorking", "python tools/google-dorking.py"),
    ("47", "Camera Hacking", "python tools/cam-hackers.py"),
]

def print_menu():
    print("\033[92m" + "="*75)
    print("\033[91m{:^75}".format("F S O C I E T Y  |  TOOLKIT"))
    print("\033[92m" + "="*75)

    for i in range(0, len(TOOLS), 2):
        left = f"[{TOOLS[i][0]}] {TOOLS[i][1]:30}"
        right = f"[{TOOLS[i+1][0]}] {TOOLS[i+1][1]}" if i+1 < len(TOOLS) else ""
        print(f"\033[97m{left}   {right}")

    print("\033[92m" + "-"*75)
    print("\033[93m[88] Banner   [99] About   [00] Exit   [?] Help")
    print("\033[92m" + "="*75)

# ========= MAIN LOOP =========
try:
    while True:
        clear()
        print_menu()
        choice = input("\n\033[95m[?] Select Option → ")

        if choice == "00":
            slowprint("\033[97m[*] Thank You, Visit Again...")
            sys.exit()

        if choice in ("?", "??"):
            slowprint("\033[92m[*] 01–47 : Main Tools")
            slowprint("[*] Yellow = GUI tools")
            input("\nPress Enter to return")
            continue

        if choice == "88":
            os.system("python tools/fsociety-logo.py")
            input("\nPress Enter")
            continue

        if choice == "99":
            slowprint("\033[95mFsociety is a fictional hacker group from Mr.Robot.")
            input("\nPress Enter")
            continue

        for num, name, cmd in TOOLS:
            if choice == num:
                clear()
                os.system(cmd)
                input("\n\033[97mPress Enter to return to menu")
                break

except KeyboardInterrupt:
    slowprint("\n\033[91m[-] Exiting...")
    sys.exit()
