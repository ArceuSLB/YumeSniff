import argparse
from utils import osint_tools
import os
from datetime import datetime

def save_output(domain, ip, dig, whois_data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"outputs/{domain.replace('.', '_')}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"[+] Domain: {domain}\n")
        f.write(f"[+] IP: {ip}\n\n")
        f.write(f"[+] DIG Lookup:\n{dig}\n\n")
        f.write(f"[+] WHOIS Info:\n{whois_data}\n")
    print(f"\n[✔] Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Yumesniff OSINT Scanner")
    parser.add_argument("--url", required=True, help="Domain or URL to scan (e.g. example.com)")
    args = parser.parse_args()

    domain = args.url.replace("http://", "").replace("https://", "").split("/")[0]

    print(f"[•] Scanning domain: {domain}")

    ip = osint_tools.get_ip(domain)
    dig = osint_tools.dig_lookup(domain)
    whois_data = osint_tools.get_whois(domain)

    save_output(domain, ip, dig, whois_data)

if __name__ == "__main__":
    main()

