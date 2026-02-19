import os
import sys
import subprocess
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print(Fore.GREEN + r"""
   ███████╗██╗  ██╗███████╗██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
   ██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
   ███████╗███████║█████╗  ██████╔╝██║     ██║   ██║██║     █████╔╝ 
   ╚════██║██╔══██║██╔══╝  ██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
   ███████║██║  ██║███████╗██║  ██║███████╗╚██████╔╝╚██████╗██║  ██╗
   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                OSINT USERNAME SEARCH TOOL WITH SHERLOCK BY UNKNOW23

                           https://github.com/Charl-23

    """)

def main():
    clear()
    banner()

    username = input(Fore.CYAN + "[?] Enter username to search : ").strip()

    if not username:
        print(Fore.RED + "[-] Username cannot be empty")
        sys.exit(1)

    print(Fore.GREEN + f"[+] Launching Sherlock for: {username}\n")

    try:
        subprocess.run(
            ["sherlock", "--nsfw", "--timeout", "1", username],
            check=False
        )
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user")
    except FileNotFoundError:
        print(Fore.RED + "[-] Sherlock not found. Is it installed and in PATH ?")

if __name__ == "__main__":
    main()
