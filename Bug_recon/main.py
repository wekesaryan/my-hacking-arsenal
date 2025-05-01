import subprocess
import requests
import dns.resolver

# Subdomain Enumeration
def enumerate_subdomains(domain):
    print(f"Enumerating subdomains for {domain}...")
    subdomains = ["www", "mail", "ftp", "test"]  # Example subdomains
    found_subdomains = []
    for subdomain in subdomains:
        try:
            full_domain = f"{subdomain}.{domain}"
            dns.resolver.resolve(full_domain)
            print(f"Subdomain found: {full_domain}")
            found_subdomains.append(full_domain)
        except dns.resolver.NXDOMAIN:
            pass
    if found_subdomains:
        print(f"Total subdomains found: {len(found_subdomains)}")
    else:
        print("No subdomains found.")
    return found_subdomains

# Port Scanning
def scan_ports(domain):
    print(f"Scanning ports for {domain}...")
    try:
        result = subprocess.run(
            ['nmap', '-p', '1-1000', domain], capture_output=True, text=True)
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("No ports detected or scan failed.")
    except Exception as e:
        print(f"Error during port scanning: {e}")

# Fetches HTTP headers to identify possible security misconfigurations
def check_vulnerabilities(url):
    print(f"Checking vulnerabilities for {url}...")
    try:
        response = requests.get(url)
        if response.headers:
            print("HTTP Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
        else:
            print("No headers received from the server.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

# List and Execute Functions
def list_functions():
    print("\nAvailable Functions:")
    print("1. Subdomain Enumeration")
    print("2. Port Scanning using Nmap")
    print("3. Fetch HTTP Header")
    print("4. Exit")

# Main Function
def main():
    print(r"""

██████  ██    ██  ██████      ██████  ███████  ██████  ██████  ███    ██ 
██   ██ ██    ██ ██           ██   ██ ██      ██      ██    ██ ████   ██ 
██████  ██    ██ ██   ███     ██████  █████   ██      ██    ██ ██ ██  ██ 
██   ██ ██    ██ ██    ██     ██   ██ ██      ██      ██    ██ ██  ██ ██ 
██████   ██████   ██████      ██   ██ ███████  ██████  ██████  ██   ████                                                                                                                                           
  
  """)

    print("Example URL format: https://example.com or http://example.com")
    target_url = input("Enter the full target URL: ")  # Input full URL

    while True:
        list_functions()
        choice = input("\nChoose a function to run (1-4): ")
        if choice == "1":
            target_domain = target_url.split("://")[-1]  # Extract domain from the URL
            enumerate_subdomains(target_domain)
        elif choice == "2":
            target_domain = target_url.split("://")[-1]  # Extract domain from the URL
            scan_ports(target_domain)
        elif choice == "3":
            check_vulnerabilities(target_url)
        elif choice == "4":
            print("Exiting script. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# Common vulnerabilities check tool to add to the script:
'''
- Subdomain enumeration
- WHOIS Lookup
- DNS Lookup & Reverse DNS Lookup
- Gathering metadata from public sources i.e emails, names, etc.
- SSL/TLS certificate information
- Network scans i.e services, ports, etc.
- Web application vulnerabilities i.e. SQLi, XSS, CSRF, RCE, SSRF, etc.
- Directory Brute force
- Directory Traversal
- Insecure Direct Object References (IDOR)
- Security Misconfiguration
- Insufficient Logging & Monitoring
'''

# You can also add third-party tools API intergrations like:
'''
- Amass
- Exiftool
- Nuclei
- Nikto
- Nmap
- Securitytails
- Shodan
- VirusTotal
'''



