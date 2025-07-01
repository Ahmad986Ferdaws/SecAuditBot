# app/scanner.py

import nmap
import shodan
import os

SHODAN_API_KEY = os.getenv(\"SHODAN_API_KEY\")
shodan_api = shodan.Shodan(SHODAN_API_KEY)

def run_nmap_scan(target=\"127.0.0.1\", ports=\"1-1024\"):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=f\"-p {ports}\")
    return nm[target]

def check_shodan_ip(ip):
    result = shodan_api.host(ip)
    return result

if __name__ == \"__main__\":
    target_ip = \"scanme.nmap.org\"
    print(f\"Running Nmap scan for {target_ip}...\")
    nmap_results = run_nmap_scan(target_ip)
    print(nmap_results)

    print(f\"Checking Shodan for {target_ip}...\")
    shodan_results = check_shodan_ip(target_ip)
    print(shodan_results)
