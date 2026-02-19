import tls_client, requests
from datetime import datetime
import ctypes, json, os, time, random, re, sys
import concurrent.futures, fade
from urllib.parse import quote
import platform

# Configuration console title selon OS
def set_console_title(title: str):
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        os.system(f'echo -ne "\\033]0;{title}\\007"')

# Couleurs console 
red = '\033[38;2;255;0;0m(-)\033[0m'     # rouge pur
green = '\033[38;2;0;255;0m(+)\033[0m'   # vert pur
blue = '\033[38;2;0;128;255m(+)\033[0m'  # bleu cyan
yellow = '\033[38;2;255;255;0m(!)\033[0m' # jaune vif

# Couleurs Banniere
def gradient_green_to_darkblue(text):
    length = len(text)
    result = ""
    for i, char in enumerate(text):
        r = 0
        g = int(255 * (1 - i / (length - 1)))
        b = int(139 * (i / (length - 1)))
        result += f"\033[38;2;{r};{g};{b}m{char}"
    result += "\033[0m"
    return result

# Bannière avec fade 
banner_ascii = r"""
 ███████████  ███  █████      ███████████          █████               █████    ███    █████
░█░░░███░░░█ ░░░  ░░███      ░█░░░███░░░█         ░░███               ░███░    ░███   ░░░███
░   ░███  ░  ████  ░███ █████░   ░███  ░   ██████  ░███ █████         ░███     ░███     ░███
    ░███    ░░███  ░███░░███     ░███     ███░░███ ░███░░███          ░███     ░███     ░███
    ░███     ░███  ░██████░      ░███    ░███ ░███ ░██████░           ░███     ░███     ░███
    ░███     ░███  ░███░░███     ░███    ░███ ░███ ░███░░███          ░███     ░░░      ░███
    █████    █████ ████ █████    █████   ░░██████  ████ █████         ░█████    ███    █████
   ░░░░░    ░░░░░ ░░░░ ░░░░░    ░░░░░     ░░░░░░  ░░░░ ░░░░░          ░░░░░    ░░░    ░░░░░ 

MASS REPORT TOOL MODIFIED BY UNKNOW23"""

print(gradient_green_to_darkblue(banner_ascii))

# Charger config.json 
if not os.path.exists('config.json'):
    print(f"{red} config.json not found. Please create one with your proxy config or leave blank for proxy rotation.")
    sys.exit()

with open('config.json') as f:
    config = json.load(f)

#  Compteur global 
class Counter:
    success = 0
    failed = 0
    total = 0

# Utilitaires 
class Utils:

    @staticmethod
    def update_console_title():
        set_console_title(f"TikTok Mass Reporter | Success: {Counter.success} | Failed: {Counter.failed} | Total: {Counter.total}")

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_timestamp():
        return f'[\x1b[90m{datetime.now().strftime("%H:%M:%S")}\x1b[0m]'

    @staticmethod
    def load_proxies(filename="proxies.txt"):
        if not os.path.isfile(filename):
            print(f"{red} Proxy file '{filename}' not found!")
            return []
        with open(filename, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"{blue} Debug: Loaded {len(proxies)} proxies from {filename}")
        return proxies

    @staticmethod
    def fetch_free_proxies(filename="proxies.txt"):
        free_api = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all'
        try:
            resp = requests.get(free_api, timeout=10)
            if resp.status_code == 200:
                with open(filename, "w") as f:
                    f.write(resp.text)
                print(f"{green} Successfully fetched free proxies and saved to {filename}")
            else:
                print(f"{red} Failed to fetch proxies, status code: {resp.status_code}")
        except Exception as e:
            print(f"{red} Exception during proxy fetch: {e}")

# Générateur d'URL report à partir d'un pseudo
def generate_report_url(username: str, reason_code: int) -> str:
    encoded_username = quote(username)
    # Exemple d'URL (à adapter )
    base_url = (
        "https://www.tiktok.com/node/report/commit"
        "?nickname={nickname}&reason={reason}"
    )
    return base_url.format(nickname=encoded_username, reason=reason_code)

# Fonction principale de report 
def report(url: str, reason_code: int, proxies: list, use_proxy_from_config: bool):
    try:
        Counter.total += 1

        session = tls_client.Session(client_identifier="chrome112", random_tls_extension_order=True)

        # Gestion proxy
        if use_proxy_from_config and 'proxy' in config and config['proxy']:
            proxy = config['proxy']
            # Formatage proxy
            if "@" in proxy:
                user_pass, ip_port = proxy.split("@")
                user, password = user_pass.split(":")
                ip, port = ip_port.split(":")
                proxy_string = f"http://{user}:{password}@{ip}:{port}"
            else:
                ip, port = proxy.split(":")
                proxy_string = f"http://{ip}:{port}"
            session.proxies = {"http": proxy_string, "https": proxy_string}
            print(f"{Utils.get_timestamp()} {blue}  Using proxy from config: {proxy_string}")

        else:
            if not proxies:
                print(f"{Utils.get_timestamp()} {red} No proxies available!")
                Counter.failed += 1
                Utils.update_console_title()
                return
            proxy = random.choice(proxies)
            proxy_string = f"http://{proxy}"
            session.proxies = {"http": proxy_string, "https": proxy_string}
            print(f"{Utils.get_timestamp()} {blue}  Using random proxy: {proxy_string}")

        # Envoi de la requête
        response = session.get(url)

        if response.status_code == 200 and ("Thanks for your feedback" in response.text or "success" in response.text.lower()):
            Counter.success += 1
            print(f"{Utils.get_timestamp()} {green} [+] Report sent (#{Counter.total})")
        else:
            Counter.failed += 1
            print(f"{Utils.get_timestamp()} {red} (-) Report failed (#{Counter.total})")

        Utils.update_console_title()

    except Exception as e:
        Counter.failed += 1
        print(f"{Utils.get_timestamp()} {red} (-) Error during report (#{Counter.total}): {e}")
        Utils.update_console_title()


if __name__ == "__main__":
    Utils.clear_console()
    print(banner_ascii)

    # Choix threads
    try:
        thread_count = int(input(f"{Utils.get_timestamp()} {blue} Enter the number of threads: "))
    except ValueError:
        print(f"{Utils.get_timestamp()} {red} Invalid input for thread count.")
        sys.exit()

    # Choix pseudo TikTok
    username = input(f"{Utils.get_timestamp()} {blue} Enter the TikTok username (without @): ").strip()

    # Liste des reasons
    report_types = {
        90013: "Violence",
        90014: "Sexual Abuse",
        90016: "Animal Abuse",
        90017: "Criminal Activities",
        9020: "Hate",
        9007: "Bullying",
        90061: "Suicide Or Self-Harm",
        90064: "Dangerous Content",
        90084: "Sexual Content",
        90085: "Porn",
        90037: "Drugs",
        90038: "Firearms Or Weapons",
        9018: "Sharing Personal Info",
        90015: "Human Exploitation",
        91015: "Under Age"
    }

    print("\nAvailable report types:")
    for code, name in report_types.items():
        print(f"{code}: {name}")

    try:
        reason_code = int(input(f"{Utils.get_timestamp()} {blue} Enter the reason code from the list above: "))
        if reason_code not in report_types:
            raise ValueError()
    except ValueError:
        print(f"{Utils.get_timestamp()} {red} Invalid reason code.")
        sys.exit()

    # Génération de l’URL de report
    report_url = generate_report_url(username, reason_code)
    print(f"{Utils.get_timestamp()} {green} Generated report URL: {report_url}")

    # Charger proxies
    proxies = Utils.load_proxies()
    if not proxies:
        print(f"{yellow} Proxy list empty or not found, trying to fetch free proxies...")
        Utils.fetch_free_proxies()
        proxies = Utils.load_proxies()
        if not proxies:
            print(f"{red} No proxies available after fetching. Exiting.")
            sys.exit()

    # Demander si on veut utiliser proxy unique (config.json) ou rotation proxies
    use_proxy_from_config = False
    if 'proxy' in config and config['proxy']:
        choice = input(f"{Utils.get_timestamp()} {blue} Use single proxy from config.json? (y/N): ").strip().lower()
        if choice == 'y':
            use_proxy_from_config = True

    print(f"{Utils.get_timestamp()} {blue} Starting reports with {thread_count} threads...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        while True:
            executor.submit(report, report_url, reason_code, proxies, use_proxy_from_config)

