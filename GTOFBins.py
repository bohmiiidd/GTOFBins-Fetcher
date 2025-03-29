import requests
import argparse
import re
import sys
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)

GTFO_BASE_URL = "https://gtfobins.github.io/gtfobins/{}/"

def print_banner():
    banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════╗
{Fore.CYAN}║    {Fore.YELLOW}🚀 GTFOBins Exploit Finder {Fore.CYAN}🚀               ║
{Fore.CYAN}║   {Fore.WHITE}Find privilege escalation tricks! {Fore.RED}⚡   {Fore.CYAN}      ║
{Fore.CYAN}║                                                ║
{Fore.CYAN}║       {Fore.MAGENTA}Developed by {Fore.GREEN}Ahmed Abd       {Fore.CYAN}            ║
{Fore.CYAN}╚════════════════════════════════════════════════╝
    """
    print(banner)

def extract_bin_name(raw_path):
    """Extracts 'mount' from '/snap/core/10185/bin/mount'"""
    return re.sub(r'^.*/([^/]+)$', r'\1', raw_path.strip())

def check_bin(bin_name):
    clean_name = extract_bin_name(bin_name)
    url = GTFO_BASE_URL.format(clean_name)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            print(f"{Fore.RED}[-] Binary '{clean_name}' not found in GTFOBins. {Fore.BLUE}🤷‍♂️")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for h2 in soup.find_all('h2'):
            section = h2.text.strip()
            code_blocks = h2.find_next('pre')
            if code_blocks:
                exploits = code_blocks.get_text().strip()
                emoji = "🔴" if "suid" in section.lower() else "🔵" if "sudo" in section.lower() else "🟢"
                results.append(f"{Fore.MAGENTA}>>> {emoji} {Fore.CYAN}{section.upper()} {Fore.WHITE}:\n{Fore.GREEN}{exploits}\n")

        if results:
            print(f"\n{Fore.YELLOW}🎯 Results for {Fore.WHITE}'{clean_name}' {Fore.YELLOW}👇\n")
            print("\n".join(results))
        else:
            print(f"{Fore.YELLOW}[!] No known exploits for {Fore.WHITE}'{clean_name}'. {Fore.BLUE}Maybe safe? 🛡️")

    except requests.RequestException as e:
        print(f"{Fore.RED}💥 Network error checking '{clean_name}': {e}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description=f"{Fore.GREEN}GTFOBins Exploit Checker {Fore.WHITE}| {Fore.YELLOW}By Ahmed Abd")
    parser.add_argument("--bin", help=f"{Fore.WHITE}Check binaries (comma-separated) {Fore.GREEN}e.g., find,vim,awk")
    parser.add_argument("--file", help=f"{Fore.WHITE}Check binaries from a file {Fore.GREEN}e.g., bins.txt")
    args = parser.parse_args()

    try:
        if args.bin:
            for bin_name in args.bin.split(','):
                check_bin(bin_name.strip())
        elif args.file:
            print(f"\n{Fore.BLUE}📂 Reading binaries from file: {Fore.WHITE}{args.file}\n")
            with open(args.file, 'r') as f:
                for line in f:
                    if line.strip():
                        check_bin(line.strip())
        else:
            print(f"\n{Fore.RED}❌ Usage: {Fore.WHITE}python GTOFBins.py {Fore.GREEN}--bin <bin1,bin2> {Fore.WHITE}or {Fore.GREEN}--file <file>")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🛑 Keyboard interrupt detected. Exiting...")
    finally:
        print(f"\n{Fore.YELLOW}👋 Goodbye! Happy hacking!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🛑 Keyboard interrupt detected. Exiting...")
        print(f"{Fore.YELLOW}👋 Goodbye!\n")
        sys.exit(0)
